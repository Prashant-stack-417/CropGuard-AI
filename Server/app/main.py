"""
CropGuard AI — FastAPI Application Entry Point
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS, LOG_LEVEL
from app.database import connect_db, close_db
from app.services.ml_service import load_model, is_model_loaded

# ── Logging ───────────────────────────────────────────────────────────
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s │ %(name)-20s │ %(levelname)-7s │ %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("cropguard")


# ── Lifespan ──────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    logger.info("🌱 Starting CropGuard AI...")

    # Connect to MongoDB
    await connect_db()
    logger.info("✅ MongoDB connected")

    # Load ML model
    model_loaded = load_model()
    if model_loaded:
        logger.info("✅ ML model loaded — real inference active")
    else:
        logger.info("🎭 ML model not found — running in DEMO mode")

    yield

    # Shutdown
    await close_db()
    logger.info("👋 CropGuard AI shut down")


# ── App ───────────────────────────────────────────────────────────────
app = FastAPI(
    title="CropGuard AI",
    description="Indian Crop Disease Detection & Smart Treatment Recommendation System",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Register routes ───────────────────────────────────────────────────
from app.routes.auth_routes import router as auth_router
from app.routes.predict_routes import router as predict_router
from app.routes.history_routes import router as history_router
from app.routes.disease_routes import router as disease_router

app.include_router(auth_router)
app.include_router(predict_router)
app.include_router(history_router)
app.include_router(disease_router)


# ── Root health check ─────────────────────────────────────────────────
@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "CropGuard AI",
        "version": "1.0.0",
        "model_loaded": is_model_loaded(),
        "mode": "inference" if is_model_loaded() else "demo",
    }


@app.get("/api/status", tags=["Health"])
async def api_status():
    return {
        "api": "running",
        "model": "loaded" if is_model_loaded() else "demo_mode",
        "endpoints": [
            "POST /api/register",
            "POST /api/login",
            "POST /api/predict",
            "GET  /api/history",
            "GET  /api/diseases",
            "GET  /api/diseases/{class_key}",
            "GET  /api/crops",
        ],
    }
