"""
ML inference service using PyTorch MobileNetV2.
Falls back to seeded-random demo mode when model files are missing.
"""

import io
import json
import os
import random
import logging
from pathlib import Path
from typing import Optional

from PIL import Image

from ..config import settings
from .disease_data import DISEASE_CATALOGUE, get_class_keys

logger = logging.getLogger(__name__)

# Module-level model state (loaded once at startup)
_model = None
_class_map: dict[int, str] = {}   # {int_index: disease_key}
_device = None
_demo_mode = False


def _load_model():
    global _model, _class_map, _device, _demo_mode

    model_path = Path(settings.MODEL_PATH)
    class_map_path = Path(settings.CLASS_MAP_PATH)

    if not model_path.exists() or not class_map_path.exists():
        logger.warning(
            "Model files not found (%s, %s). Running in DEMO mode.",
            model_path, class_map_path,
        )
        _demo_mode = True
        return

    try:
        import torch
        import torchvision.models as models
        from torchvision import transforms  # noqa: F401 – confirm available

        _device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Load class map — supports both {idx: key} and {key: idx} formats
        with open(class_map_path) as f:
            raw: dict = json.load(f)

        first_key = next(iter(raw))
        if first_key.isdigit():
            # {idx_str: disease_key}
            _class_map = {int(k): v for k, v in raw.items()}
        else:
            # {disease_key: idx}
            _class_map = {int(v): k for k, v in raw.items()}

        num_classes = len(_class_map)

        # Build MobileNetV2 with matching head
        model = models.mobilenet_v2(weights=None)
        model.classifier[1] = __import__("torch").nn.Linear(
            model.last_channel, num_classes
        )
        model.load_state_dict(
            __import__("torch").load(model_path, map_location=_device)
        )
        model.eval()
        model.to(_device)
        _model = model
        _demo_mode = False
        logger.info("Model loaded: %d classes on %s", num_classes, _device)

    except Exception as exc:
        logger.error("Failed to load model: %s — switching to demo mode.", exc)
        _demo_mode = True


def _get_transforms():
    from torchvision import transforms
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])


def _demo_predict(image_bytes: bytes) -> dict:
    """Return a deterministic-random result based on image hash for demo mode."""
    seed = sum(image_bytes[:256])  # simple hash
    rng = random.Random(seed)
    keys = get_class_keys()
    key = rng.choice(keys)
    confidence = round(rng.uniform(0.65, 0.99), 4)
    disease = DISEASE_CATALOGUE[key]
    return {
        "disease_key": key,
        "confidence": confidence,
        **disease,
    }


def predict(image_bytes: bytes) -> dict:
    """Run inference on raw image bytes. Returns prediction dict."""
    global _model

    if _model is None and not _demo_mode:
        _load_model()

    if _demo_mode:
        return _demo_predict(image_bytes)

    import torch

    # Preprocess
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    transform = _get_transforms()
    tensor = transform(image).unsqueeze(0).to(_device)

    with torch.no_grad():
        logits = _model(tensor)
        probs = torch.softmax(logits, dim=1)[0]
        top_idx = int(torch.argmax(probs).item())
        confidence = float(probs[top_idx].item())

    disease_key = _class_map.get(top_idx, "unknown")
    disease = DISEASE_CATALOGUE.get(disease_key, {})

    return {
        "disease_key": disease_key,
        "confidence": round(confidence, 4),
        **disease,
    }


# Trigger model load once this module is imported
_load_model()
