import io
import logging
import random
from typing import Optional

import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("cropguard")

# ---------------------------------------------------------------------------
# Model / image configuration
# ---------------------------------------------------------------------------
# Standard input size expected by most crop-disease CNNs (e.g. ResNet, EfficientNet)
IMAGE_SIZE: tuple[int, int] = (224, 224)

# ImageNet mean/std used for normalisation – update if your model uses different values
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

# Maximum accepted upload size (10 MB)
MAX_FILE_SIZE_BYTES: int = 10 * 1024 * 1024

# Predictions below this threshold are reported as "Uncertain"
CONFIDENCE_THRESHOLD: float = 0.50

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(title="CropGuard AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Response schema
# ---------------------------------------------------------------------------
class DetectionResult(BaseModel):
    diseaseName: str
    cropName: str
    confidence: int          # 0-100
    status: str              # "Healthy" | "Diseased" | "Uncertain"
    severity: str            # "None" | "Low" | "Medium" | "High"
    description: str
    treatments: list[str]
    prevention: list[str]
    spreadRisk: str          # "None" | "Low" | "Medium" | "High"


# ---------------------------------------------------------------------------
# Disease knowledge base
#
# Keys are integer class indices that match the output layer order of your ML
# model.  When you train / export a model, make sure its class ordering aligns
# with the indices below.  Add or remove entries as needed.
# ---------------------------------------------------------------------------
DISEASE_CLASSES: dict[int, DetectionResult] = {
    0: DetectionResult(
        diseaseName="Late Blight",
        cropName="Tomato",
        confidence=0,           # overwritten at inference time by model softmax score
        status="Diseased",
        severity="High",
        description=(
            "Late blight is a devastating disease that affects tomato plants, causing "
            "dark lesions on leaves and stems. It spreads rapidly in humid conditions "
            "and can destroy entire crops if left untreated."
        ),
        treatments=[
            "Remove and destroy infected plant parts immediately",
            "Apply copper-based fungicides every 7-10 days",
            "Ensure proper plant spacing for air circulation",
            "Avoid overhead watering to reduce leaf wetness",
            "Use disease-resistant tomato varieties in future plantings",
        ],
        prevention=[
            "Plant certified disease-free transplants",
            "Apply preventive fungicides before the rainy season",
            "Rotate tomatoes with non-solanaceous crops each season",
            "Remove crop debris after harvest to eliminate overwintering spores",
        ],
        spreadRisk="High",
    ),
    1: DetectionResult(
        diseaseName="Powdery Mildew",
        cropName="Cucumber",
        confidence=0,
        status="Diseased",
        severity="Medium",
        description=(
            "Powdery mildew appears as white, powdery spots on leaves and stems. "
            "It thrives in warm, dry conditions with high humidity and can reduce "
            "crop yield significantly."
        ),
        treatments=[
            "Apply sulfur or potassium bicarbonate fungicides",
            "Remove heavily infected leaves",
            "Improve air circulation around plants",
            "Water plants at the base, not from above",
            "Apply neem oil spray as a natural alternative",
        ],
        prevention=[
            "Choose mildew-resistant cucumber varieties",
            "Avoid overcrowding plants to improve airflow",
            "Apply preventive sulfur sprays during warm, dry weather",
            "Keep garden free of weeds that may host the pathogen",
        ],
        spreadRisk="Medium",
    ),
    2: DetectionResult(
        diseaseName="Leaf Rust",
        cropName="Wheat",
        confidence=0,
        status="Diseased",
        severity="High",
        description=(
            "Leaf rust causes orange-brown pustules on wheat leaves, reducing "
            "photosynthesis and grain quality. It spreads through wind-borne spores."
        ),
        treatments=[
            "Apply triazole fungicides at early infection stages",
            "Use rust-resistant wheat varieties",
            "Practice crop rotation",
            "Remove volunteer wheat plants that harbor spores",
            "Monitor fields regularly for early detection",
        ],
        prevention=[
            "Plant certified rust-resistant wheat varieties",
            "Avoid planting wheat near alternate hosts such as barberry",
            "Apply fungicide seed treatment before sowing",
            "Scout fields early in the season for first signs of infection",
        ],
        spreadRisk="High",
    ),
    3: DetectionResult(
        diseaseName="Bacterial Leaf Blight",
        cropName="Rice",
        confidence=0,
        status="Diseased",
        severity="Medium",
        description=(
            "Bacterial leaf blight turns rice leaves yellow and then brown, "
            "starting from the tips. It is most severe during the wet season "
            "and can cause significant yield loss."
        ),
        treatments=[
            "Use certified, disease-free seeds",
            "Apply copper-based bactericides",
            "Drain fields during tillering stage",
            "Avoid excessive nitrogen fertilization",
            "Plant resistant rice varieties",
        ],
        prevention=[
            "Source seeds only from certified, disease-free suppliers",
            "Avoid injuries to plants during transplanting",
            "Maintain balanced soil nutrition to strengthen plant immunity",
            "Ensure good field drainage to minimise waterlogging",
        ],
        spreadRisk="Medium",
    ),
    4: DetectionResult(
        diseaseName="Healthy",
        cropName="Rice",
        confidence=0,
        status="Healthy",
        severity="None",
        description=(
            "The plant appears healthy with no visible signs of disease. "
            "Continue regular monitoring and maintain good agricultural practices."
        ),
        treatments=[
            "Continue regular monitoring for any changes",
            "Maintain proper irrigation and drainage",
            "Apply balanced fertilizers as per soil test",
            "Practice preventive pest management",
            "Ensure proper plant spacing",
        ],
        prevention=[
            "Rotate crops each season to break disease cycles",
            "Use certified seeds and healthy planting material",
            "Maintain field hygiene by removing dead plant matter",
            "Conduct regular soil health tests and amend as needed",
        ],
        spreadRisk="None",
    ),
}

# ---------------------------------------------------------------------------
# Model loader
# ---------------------------------------------------------------------------
# _model holds the loaded ML model instance (None until load_model() is called).
_model: Optional[object] = None


def load_model() -> Optional[object]:
    """
    Load and return the trained ML model.

    ── How to integrate your model ──────────────────────────────────────────
    TensorFlow / Keras example:
        import tensorflow as tf
        model = tf.keras.models.load_model("model/cropguard_model.h5")
        return model

    PyTorch example:
        import torch
        from model_definition import CropGuardNet   # your architecture file
        model = CropGuardNet()
        model.load_state_dict(torch.load("model/cropguard_weights.pth"))
        model.eval()
        return model

    ONNX Runtime example:
        import onnxruntime as ort
        session = ort.InferenceSession("model/cropguard.onnx")
        return session
    ─────────────────────────────────────────────────────────────────────────
    """
    # TODO: replace the line below with actual model loading once available
    logger.warning("No ML model loaded – running in DEMO (random) mode.")
    return None


# Load model once at startup
_model = load_model()

# ---------------------------------------------------------------------------
# Image preprocessing
# ---------------------------------------------------------------------------

def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Resize and normalise a PIL image into a float32 array ready for inference.

    Returns shape: (1, IMAGE_SIZE[0], IMAGE_SIZE[1], 3)  — batch-of-one, channels-last.
    Adjust the reshape / transpose if your model expects channels-first (e.g. PyTorch).
    """
    image = image.resize(IMAGE_SIZE, resample=Image.BILINEAR)
    arr = np.array(image, dtype=np.float32) / 255.0          # → [0, 1]
    arr = (arr - IMAGENET_MEAN) / IMAGENET_STD               # normalise
    return np.expand_dims(arr, axis=0)                        # add batch dim


# ---------------------------------------------------------------------------
# ML inference
# ---------------------------------------------------------------------------

def run_model(image: Image.Image) -> DetectionResult:
    """
    Pre-process *image* and run it through the ML model.

    ── Swap-in instructions when your model is ready ────────────────────────
    1.  Call load_model() in the startup block above and assign to _model.
    2.  Replace the DEMO block below with actual inference, for example:

        TensorFlow / Keras:
            tensor = preprocess_image(image)            # shape (1,224,224,3)
            probs  = _model.predict(tensor)[0]          # shape (num_classes,)
            class_idx   = int(np.argmax(probs))
            confidence  = float(probs[class_idx])

        PyTorch:
            import torch
            tensor = torch.from_numpy(preprocess_image(image))  # (1,3,H,W) if channels-first
            with torch.no_grad():
                probs = torch.softmax(_model(tensor), dim=1)[0]
            class_idx  = int(probs.argmax())
            confidence = float(probs[class_idx])

        ONNX Runtime:
            input_name = _model.get_inputs()[0].name
            probs      = _model.run(None, {input_name: preprocess_image(image)})[0][0]
            class_idx  = int(np.argmax(probs))
            confidence = float(probs[class_idx])

    3.  Then build and return the result:

        if confidence < CONFIDENCE_THRESHOLD:
            return DetectionResult(
                diseaseName="Uncertain",
                cropName="Unknown",
                confidence=int(confidence * 100),
                status="Uncertain",
                description="The model could not confidently identify the disease. "
                            "Please upload a clearer image of the crop leaf.",
                treatments=["Consult a local agricultural expert for diagnosis."],
            )

        template = DISEASE_CLASSES[class_idx]
        return template.model_copy(update={"confidence": int(confidence * 100)})
    ─────────────────────────────────────────────────────────────────────────
    """

    if _model is not None:
        # ── Real inference path (activated once _model is loaded) ──────────
        tensor      = preprocess_image(image)
        # probs     = <call your model here>(tensor)   ← replace this line
        # class_idx = int(np.argmax(probs))
        # confidence= float(probs[class_idx])
        # … (see docstring above)
        pass  # remove this line when implementing

    # ── DEMO path: random selection until a real model is integrated ────────
    logger.info("DEMO mode: returning a random disease result.")
    template = random.choice(list(DISEASE_CLASSES.values()))
    demo_confidence = random.randint(75, 98)
    return template.model_copy(update={"confidence": demo_confidence})


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
def health_check():
    """Basic liveness probe; also reports whether the ML model is loaded."""
    return {
        "status": "ok",
        "service": "CropGuard AI",
        "model_loaded": _model is not None,
        "mode": "production" if _model is not None else "demo",
    }


@app.post("/detect", response_model=DetectionResult)
async def detect_disease(file: UploadFile = File(...)):
    """
    Accepts a crop-leaf image and returns a disease-detection result.

    - **file**: image file (JPEG, PNG, WEBP, …), max 10 MB
    """
    # ── 1. Validate MIME type ───────────────────────────────────────────────
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")

    # ── 2. Read bytes & enforce file-size limit ─────────────────────────────
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"Image exceeds maximum allowed size of {MAX_FILE_SIZE_BYTES // (1024*1024)} MB.",
        )

    # ── 3. Decode image ─────────────────────────────────────────────────────
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as exc:
        logger.warning("Image decode failed: %s", exc)
        raise HTTPException(status_code=400, detail="Could not decode the image. Please upload a valid image file.")

    logger.info(
        "Received image | filename=%s | size=%dx%d | content_type=%s",
        file.filename, image.width, image.height, file.content_type,
    )

    # ── 4. Run inference ─────────────────────────────────────────────────────
    result = run_model(image)
    logger.info(
        "Prediction | disease=%s | crop=%s | confidence=%d%% | status=%s",
        result.diseaseName, result.cropName, result.confidence, result.status,
    )
    return result
