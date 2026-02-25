"""
ML Inference Service
---------------------
Loads the trained CNN model (MobileNetV2 / EfficientNet / ResNet50)
and runs prediction on uploaded images.  Falls back to demo mode
when no model file is present.
"""

import io
import json
import random
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


# ── Model Loading ─────────────────────────────────────────────────────
def load_model():
    """
    Attempt to load the ML model at startup.
    Returns True if model loaded, False if running in demo mode.
    """
    global _model, _class_map
    model_path = Path(MODEL_PATH)

    # Try loading class map
    class_map_path = Path(CLASS_MAP_PATH)
    if class_map_path.exists():
        with open(class_map_path) as f:
            _class_map = json.load(f)
        logger.info(f"Loaded class map with {len(_class_map)} classes")

    # Try loading model
    if not model_path.exists():
        logger.warning(f"Model file not found at {model_path}. Running in DEMO mode.")
        return False

    try:
        # TensorFlow / Keras
        import tensorflow as tf

        _model = tf.keras.models.load_model(str(model_path))
        logger.info(f"✅ Model loaded from {model_path}")
        logger.info(f"   Input shape: {_model.input_shape}")
        logger.info(f"   Output classes: {_model.output_shape[-1]}")
        return True
    except ImportError:
        logger.warning("TensorFlow not installed. Trying ONNX runtime...")

    try:
        # ONNX Runtime fallback
        import onnxruntime as ort

        _model = ort.InferenceSession(str(model_path))
        logger.info(f"✅ ONNX model loaded from {model_path}")
        return True
    except ImportError:
        logger.warning("Neither TensorFlow nor ONNX runtime installed. Running in DEMO mode.")
        return False
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        return False


def is_model_loaded() -> bool:
    return _model is not None


# ── Image Preprocessing ──────────────────────────────────────────────
def preprocess_image(image: Image.Image) -> np.ndarray:
    """Preprocess image for model inference."""
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE, Image.Resampling.LANCZOS)
    arr = np.array(image, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)  # shape: (1, 224, 224, 3)


# ── Prediction ────────────────────────────────────────────────────────
def predict(image_bytes: bytes) -> dict:
    """
    Run disease prediction on image bytes.
    Returns a dict with crop_name, disease_name, confidence, and full treatment info.
    """
    image = Image.open(io.BytesIO(image_bytes))

    if _model is not None:
        result = _run_real_inference(image)
    else:
        result = _run_demo_inference()

    return result


def _run_real_inference(image: Image.Image) -> dict:
    """Run actual model inference."""
    tensor = preprocess_image(image)

    try:
        # TensorFlow model
        import tensorflow as tf

        if isinstance(_model, tf.keras.Model):
            probs = _model.predict(tensor, verbose=0)[0]
            class_idx = int(np.argmax(probs))
            confidence = float(probs[class_idx])
        else:
            raise TypeError("Unknown model type")
    except (ImportError, TypeError):
        try:
            # ONNX Runtime
            input_name = _model.get_inputs()[0].name
            probs = _model.run(None, {input_name: tensor})[0][0]
            class_idx = int(np.argmax(probs))
            confidence = float(probs[class_idx])
        except Exception as e:
            logger.error(f"Inference failed: {e}")
            return _run_demo_inference()

    # Map index to class key
    if _class_map:
        class_key = _class_map.get(str(class_idx), list(DISEASE_DATABASE.keys())[class_idx])
    else:
        class_key = CLASS_INDEX_MAP.get(class_idx, list(DISEASE_DATABASE.keys())[0])

    confidence_pct = int(confidence * 100)

    # Low confidence fallback
    if confidence < CONFIDENCE_THRESHOLD:
        return {
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
    disease_info = get_disease_info(class_key) or {}
    return _build_result(disease_info, confidence_pct)


def _run_demo_inference() -> dict:
    """Demo mode: return realistic random result."""
    logger.info("🎭 DEMO mode — returning random disease result")
    keys = list(DISEASE_DATABASE.keys())
    class_key = random.choice(keys)
    disease_info = DISEASE_DATABASE[class_key]
    confidence = random.randint(78, 97)
    return _build_result(disease_info, confidence)


def _build_result(disease_info: dict, confidence: int) -> dict:
    """Build a standardised prediction result dict."""
    is_healthy = disease_info.get("disease_name") == "Healthy"
    return {
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
