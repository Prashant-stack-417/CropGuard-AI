import io
import random
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image

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
    status: str              # "Healthy" | "Diseased"
    description: str
    treatments: list[str]


# ---------------------------------------------------------------------------
# Disease knowledge base
# Replace / extend this list with your own ML model output mapping.
# ---------------------------------------------------------------------------
DISEASE_CLASSES: list[DetectionResult] = [
    DetectionResult(
        diseaseName="Late Blight",
        cropName="Tomato",
        confidence=94,
        status="Diseased",
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
    ),
    DetectionResult(
        diseaseName="Powdery Mildew",
        cropName="Cucumber",
        confidence=89,
        status="Diseased",
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
    ),
    DetectionResult(
        diseaseName="Leaf Rust",
        cropName="Wheat",
        confidence=91,
        status="Diseased",
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
    ),
    DetectionResult(
        diseaseName="Bacterial Leaf Blight",
        cropName="Rice",
        confidence=88,
        status="Diseased",
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
    ),
    DetectionResult(
        diseaseName="Healthy",
        cropName="Rice",
        confidence=97,
        status="Healthy",
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
    ),
]


# ---------------------------------------------------------------------------
# ML inference placeholder
# ---------------------------------------------------------------------------
def run_model(image: Image.Image) -> DetectionResult:
    """
    Replace the body of this function with your actual model inference.

    Example with a TensorFlow / PyTorch model:
        tensor = preprocess(image)
        logits = model(tensor)
        class_idx = logits.argmax()
        return DISEASE_CLASSES[class_idx]
    """
    # --- Demo: random selection until a real model is integrated ---
    return random.choice(DISEASE_CLASSES)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/")
def health_check():
    return {"status": "ok", "service": "CropGuard AI"}


@app.post("/detect", response_model=DetectionResult)
async def detect_disease(file: UploadFile = File(...)):
    """
    Accepts a crop leaf image and returns a disease-detection result.

    - **file**: image file (JPEG, PNG, WEBP, …)
    """
    # Validate MIME type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")

    # Read and open image
    contents = await file.read()
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Could not decode the image.")

    # Run inference
    result = run_model(image)
    return result
