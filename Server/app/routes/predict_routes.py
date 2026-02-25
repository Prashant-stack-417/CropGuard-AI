"""
Prediction route — Accept image → Run model → Return result
"""

import logging
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from app.auth import get_current_user
from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE
from app.database import get_db
from app.services.ml_service import predict

logger = logging.getLogger("cropguard.predict")

router = APIRouter(prefix="/api", tags=["Prediction"])


@router.post("/predict")
async def predict_disease(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    """
    Accept a crop leaf image and return disease prediction with treatments.
    Authentication is optional — unauthenticated users can still predict
    but results won't be saved to history.
    """
    # ── Validate file ─────────────────────────────────────────────────
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be an image (JPEG, PNG, or WEBP)",
        )

    ext = Path(file.filename or "").suffix.lower()
    if ext and ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type '{ext}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}",
        )

    # Read and check size
    image_bytes = await file.read()
    if len(image_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)} MB",
        )

    if len(image_bytes) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty",
        )

    # ── Run prediction ────────────────────────────────────────────────
    try:
        result = predict(image_bytes)
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Prediction failed. Please try again with a different image.",
        )

    # ── Save to history (if authenticated) ────────────────────────────
    prediction_id = None
    if current_user:
        db = get_db()
        prediction_doc = {
            "user_id": current_user["_id"],
            "crop_name": result["crop_name"],
            "disease_name": result["disease_name"],
            "confidence": result["confidence"],
            "severity": result["severity"],
            "status": result["status"],
            "description": result["description"],
            "organic_treatment": result["organic_treatment"],
            "chemical_treatment": result["chemical_treatment"],
            "dosage": result["dosage"],
            "prevention": result["prevention"],
            "filename": file.filename,
            "created_at": datetime.now(timezone.utc),
        }
        insert_result = await db.predictions.insert_one(prediction_doc)
        prediction_id = str(insert_result.inserted_id)

    result["prediction_id"] = prediction_id
    result["created_at"] = datetime.now(timezone.utc).isoformat()

    return result
