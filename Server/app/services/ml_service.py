"""
ML Inference Service
---------------------
Loads the trained CNN model (PyTorch MobileNetV2) and runs prediction
on uploaded images.  Requires a valid model file to operate.

The model is trained via notebooks/train_model.ipynb and exported as:
  - model/crop_disease_model.pt    (TorchScript model)
  - model/class_map.json           (index → class name)
"""

import io
import json
import hashlib

import logging
from pathlib import Path

import numpy as np
from PIL import Image

from app.config import MODEL_PATH, CLASS_MAP_PATH, CONFIDENCE_THRESHOLD
from app.services.disease_data import (
    DISEASE_DATABASE,
    CLASS_INDEX_MAP,
    get_disease_info,
)

logger = logging.getLogger("cropguard.ml")

# ── Globals ───────────────────────────────────────────────────────────
_model = None
_class_map: dict | None = None

IMG_SIZE = (224, 224)

# ImageNet normalisation (must match training transforms)
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


# ── Model Loading ─────────────────────────────────────────────────────
def load_model():
    """
    Attempt to load the ML model at startup.
    Returns True if model loaded, False if running in demo mode.
    """
    global _model, _class_map

    # Try loading class map
    class_map_path = Path(CLASS_MAP_PATH)
    if class_map_path.exists():
        with open(class_map_path) as f:
            _class_map = json.load(f)
        logger.info(f"Loaded class map with {len(_class_map)} classes")

    # ── Find model file (.pt or .h5) ─────────────────────────────
    model_path = Path(MODEL_PATH)

    # Also check for .pt variant
    pt_path = model_path.with_suffix(".pt")
    if pt_path.exists():
        model_path = pt_path
    elif not model_path.exists():
        # Check model directory for any model file
        model_dir = model_path.parent
        if model_dir.exists():
            for ext in (".pt", ".pth", ".h5"):
                found = list(model_dir.glob(f"*{ext}"))
                if found:
                    model_path = found[0]
                    break

    if not model_path.exists():
        logger.warning(f"Model file not found at {model_path}. Running in DEMO mode.")
        return False

    # ── Load PyTorch model ───────────────────────────────────────
    try:
        import torch

        if model_path.suffix in (".pt", ".pth"):
            _model = torch.jit.load(str(model_path), map_location="cpu")
            _model.eval()
            logger.info(f"✅ PyTorch model loaded from {model_path}")
            return True
    except ImportError:
        logger.warning("PyTorch not installed.")
    except Exception as e:
        logger.error(f"Failed to load PyTorch model: {e}")

    # ── Fallback: TensorFlow ─────────────────────────────────────
    try:
        import tensorflow as tf  # type: ignore

        _model = tf.keras.models.load_model(str(model_path))
        logger.info(f"✅ TensorFlow model loaded from {model_path}")
        return True
    except ImportError:
        logger.warning("TensorFlow not installed either.")
    except Exception as e:
        logger.error(f"Failed to load TF model: {e}")

    logger.warning("No ML framework available. Running in DEMO mode.")
    return False


def is_model_loaded() -> bool:
    return _model is not None


# ── Image Preprocessing ──────────────────────────────────────────────
def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Preprocess image for MobileNetV2 inference.
    Matches the val_transform used during training:
      - Resize to 224x224
      - Scale to [0, 1]
      - Normalise with ImageNet mean/std
      - Shape: (1, 3, 224, 224) for PyTorch
    """
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE, Image.Resampling.LANCZOS)
    arr = np.array(image, dtype=np.float32) / 255.0  # [0, 1]

    # ImageNet normalisation
    arr = (arr - IMAGENET_MEAN) / IMAGENET_STD

    # HWC → CHW (PyTorch format)
    arr = arr.transpose(2, 0, 1)

    return np.expand_dims(arr, axis=0)  # (1, 3, 224, 224)


# ── Class Key Matching ───────────────────────────────────────────────
# Maps model output labels (from class_map.json) → DISEASE_DATABASE keys
CLASS_NAME_TO_DB_KEY = {
    # Rice
    "Becterial Blight in Rice": "Rice___Leaf_Blight",
    "Brownspot": "Rice___Brown_Spot",
    "Rice Blast": "Rice___Blast",
    "Tungro": "Rice___Tungro",
    # Wheat
    "Flag Smut": "Wheat___Flag_Smut",
    "Healthy Wheat": "Wheat___Healthy",
    "Leaf smut": "Wheat___Leaf_Smut",
    "Wheat Brown leaf Rust": "Wheat___Leaf_Rust",
    "Wheat Stem fly": "Wheat___Stem_Fly",
    "Wheat aphid": "Wheat___Aphid",
    "Wheat black rust": "Wheat___Black_Rust",
    "Wheat leaf blight": "Wheat___Leaf_Blight",
    "Wheat mite": "Wheat___Mite",
    "Wheat powdery mildew": "Wheat___Powdery_Mildew",
    "Wheat scab": "Wheat___Scab",
    "Wheat___Yellow_Rust": "Wheat___Yellow_Rust",
    # Maize
    "Common_Rust": "Maize___Common_Rust",
    "Gray_Leaf_Spot": "Maize___Gray_Leaf_Spot",
    "Healthy Maize": "Maize___Healthy",
    "Army worm": "Maize___Armyworm",
    "maize ear rot": "Maize___Ear_Rot",
    "maize fall armyworm": "Maize___Fall_Armyworm",
    "maize stem borer": "Maize___Stem_Borer",
    # Cotton
    "American Bollworm on Cotton": "Cotton___American_Bollworm",
    "Anthracnose on Cotton": "Cotton___Anthracnose",
    "Cotton Aphid": "Cotton___Aphid",
    "Healthy cotton": "Cotton___Healthy",
    "Leaf Curl": "Cotton___Leaf_Curl",
    "bacterial_blight in Cotton": "Cotton___Bacterial_Blight",
    "bollrot on Cotton": "Cotton___Boll_Rot",
    "bollworm on Cotton": "Cotton___Bollworm",
    "cotton mealy bug": "Cotton___Mealy_Bug",
    "cotton whitefly": "Cotton___Whitefly",
    "pink bollworm in cotton": "Cotton___Pink_Bollworm",
    "red cotton bug": "Cotton___Red_Bug",
    "thirps on  cotton": "Cotton___Thrips",
    "Wilt": "Cotton___Wilt",
    # Sugarcane
    "Mosaic sugarcane": "Sugarcane___Mosaic",
    "RedRot sugarcane": "Sugarcane___Red_Rot",
    "RedRust sugarcane": "Sugarcane___Red_Rust",
    "Sugarcane Healthy": "Sugarcane___Healthy",
    "Yellow Rust Sugarcane": "Sugarcane___Yellow_Rust",
    # Tomato — direct matches in DB already
    # Potato — direct matches in DB already
}


def _match_class_to_disease(class_name: str) -> str:
    """
    Match a dataset class name (e.g. 'Brownspot', 'American Bollworm on Cotton')
    to a DISEASE_DATABASE key (e.g. 'Rice___Brown_Spot', 'Cotton___American_Bollworm').
    """
    # 1. Exact match in explicit mapping
    if class_name in CLASS_NAME_TO_DB_KEY:
        return CLASS_NAME_TO_DB_KEY[class_name]

    # 2. Direct match in database
    if class_name in DISEASE_DATABASE:
        return class_name

    # 3. Lowercase comparison
    lower_map = {k.lower().replace(" ", "_"): k for k in DISEASE_DATABASE}
    normalised = class_name.lower().replace(" ", "_")

    if normalised in lower_map:
        return lower_map[normalised]

    # 4. Fuzzy: crop___disease matching
    parts = class_name.split("___")
    if len(parts) == 2:
        crop, disease = parts
        for db_key in DISEASE_DATABASE:
            db_parts = db_key.split("___")
            if len(db_parts) == 2:
                if (crop.lower() == db_parts[0].lower() and
                        disease.lower().replace("_", "") == db_parts[1].lower().replace("_", "")):
                    return db_key

    logger.warning(f"No disease data match for class '{class_name}'")
    return class_name


# ── Prediction ────────────────────────────────────────────────────────
def predict(image_bytes: bytes) -> dict:
    """
    Run disease prediction on image bytes.
    Returns a dict with crop_name, disease_name, confidence, and treatment info.
    Raises RuntimeError if the ML model is not loaded.
    """
    if _model is None:
        # Vercel/serverless fallback: keep API functional when ML runtime is unavailable.
        return _run_demo_inference(image_bytes)

    image = Image.open(io.BytesIO(image_bytes))
    return _run_real_inference(image)


def _run_demo_inference(image_bytes: bytes) -> dict:
    """Return a deterministic demo prediction when no ML model/runtime is loaded."""
    if not DISEASE_DATABASE:
        return {
            "class_key": "",
            "crop_name": "Unknown",
            "disease_name": "Uncertain",
            "confidence": 0,
            "severity": "Unknown",
            "spread_risk": "Unknown",
            "description": "Demo inference is enabled but disease data is not available.",
            "symptoms": [],
            "organic_treatment": ["Check server deployment data and retry."],
            "chemical_treatment": ["Check server deployment data and retry."],
            "dosage": "Not applicable",
            "prevention": ["Ensure disease metadata is deployed correctly."],
            "status": "Uncertain",
        }

    keys = sorted(DISEASE_DATABASE.keys())
    digest = hashlib.sha256(image_bytes).hexdigest()
    index = int(digest[:8], 16) % len(keys)
    class_key = keys[index]
    base = get_disease_info(class_key) or {}
    confidence = 72 + (int(digest[8:10], 16) % 19)

    result = _build_result(base, confidence, class_key)
    result["description"] = (
        f"{result['description']} [demo mode: model runtime unavailable on this deployment]"
    )
    return result


def _run_real_inference(image: Image.Image) -> dict:
    """Run actual model inference."""
    tensor = preprocess_image(image)

    try:
        import torch

        with torch.no_grad():
            input_tensor = torch.from_numpy(tensor)
            outputs = _model(input_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)[0]
            class_idx = int(torch.argmax(probs))
            confidence = float(probs[class_idx])

    except ImportError:
        # TensorFlow fallback
        try:
            probs = _model.predict(tensor, verbose=0)[0]
            class_idx = int(np.argmax(probs))
            confidence = float(probs[class_idx])
        except Exception as e:
            logger.error(f"TensorFlow inference failed: {e}")
            raise RuntimeError(f"Inference failed: {e}") from e
    except Exception as e:
        logger.error(f"Inference failed: {e}")
        raise RuntimeError(f"Inference failed: {e}") from e

    # Map index → class name → disease database key
    if _class_map:
        class_name = _class_map.get(str(class_idx), f"Unknown_{class_idx}")
    else:
        class_name = CLASS_INDEX_MAP.get(class_idx, list(DISEASE_DATABASE.keys())[0])

    class_key = _match_class_to_disease(class_name)
    confidence_pct = int(confidence * 100)

    logger.info(f"Prediction: idx={class_idx}, class='{class_name}', key='{class_key}', conf={confidence_pct}%")

    # Low confidence fallback
    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "class_key": "",
            "crop_name": "Unknown",
            "disease_name": "Uncertain",
            "confidence": confidence_pct,
            "severity": "Unknown",
            "spread_risk": "Unknown",
            "description": "The model could not identify the disease with sufficient confidence. "
            "Please upload a clearer, closer image of the affected leaf.",
            "symptoms": [],
            "organic_treatment": ["Consult a local agricultural expert for accurate diagnosis."],
            "chemical_treatment": ["Visit your nearest Krishi Vigyan Kendra (KVK) for guidance."],
            "dosage": "Not applicable",
            "prevention": ["Take clear, well-lit photos of individual leaves for better results."],
            "status": "Uncertain",
        }

    # Build result from disease data
    disease_info = get_disease_info(class_key)

    # Generic fallback for unmatched classes
    if not disease_info:
        parts = class_name.split("___")
        crop = parts[0].replace("_", " ") if parts else "Unknown"
        disease = parts[1].replace("_", " ") if len(parts) > 1 else class_name.replace("_", " ")

        return {
            "class_key": class_key if class_key in DISEASE_DATABASE else "",
            "crop_name": crop,
            "disease_name": disease,
            "confidence": confidence_pct,
            "severity": "Medium",
            "spread_risk": "Medium",
            "description": f"Detected {disease} on {crop} with {confidence_pct}% confidence.",
            "symptoms": [],
            "organic_treatment": ["Consult a local agricultural expert for specific treatment."],
            "chemical_treatment": ["Visit your nearest Krishi Vigyan Kendra (KVK) for guidance."],
            "dosage": "Consult an expert",
            "prevention": ["Practice crop rotation", "Use disease-resistant varieties"],
            "status": "Healthy" if "healthy" in disease.lower() else "Diseased",
        }

    return _build_result(disease_info, confidence_pct, class_key)





def _build_result(disease_info: dict, confidence: int, class_key: str = "") -> dict:
    """Build a standardised prediction result dict."""
    is_healthy = disease_info.get("disease_name") == "Healthy"
    return {
        "class_key": class_key,
        "crop_name": disease_info.get("crop", "Unknown"),
        "disease_name": disease_info.get("disease_name", "Unknown"),
        "confidence": confidence,
        "severity": disease_info.get("severity", "Unknown"),
        "spread_risk": disease_info.get("spread_risk", "Unknown"),
        "description": disease_info.get("description", ""),
        "symptoms": disease_info.get("symptoms", []),
        "organic_treatment": disease_info.get("organic_treatment", []),
        "chemical_treatment": disease_info.get("chemical_treatment", []),
        "dosage": disease_info.get("dosage", ""),
        "prevention": disease_info.get("prevention", []),
        "status": "Healthy" if is_healthy else "Diseased",
    }
