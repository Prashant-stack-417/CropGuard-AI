"""
Application configuration — loaded from environment variables.
"""

import os
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

# ── MongoDB ───────────────────────────────────────────────────────────
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "cropguard")

# ── JWT ───────────────────────────────────────────────────────────────
JWT_SECRET = os.getenv("JWT_SECRET", "cropguard-hackathon-secret-key-change-in-prod")
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))  # 24 hours

# ── ML Model ─────────────────────────────────────────────────────────
MODEL_PATH = os.getenv("MODEL_PATH", str(MODEL_DIR / "crop_disease_model.h5"))
CLASS_MAP_PATH = os.getenv("CLASS_MAP_PATH", str(MODEL_DIR / "class_map.json"))
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.40"))

# ── Upload ────────────────────────────────────────────────────────────
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", str(10 * 1024 * 1024)))  # 10 MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

# ── Server ────────────────────────────────────────────────────────────
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
