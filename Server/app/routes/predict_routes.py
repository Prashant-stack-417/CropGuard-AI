from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.params import Depends

from ..auth import get_optional_user
from ..database import get_db
from ..models import PredictResponse, TreatmentInfo
from ..services import ml_service

router = APIRouter(tags=["prediction"])

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("/predict", response_model=PredictResponse)
async def predict(
    file: UploadFile = File(...),
    current_user: Optional[dict] = Depends(get_optional_user),
):
    # Validate file type
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported file type: {file.content_type}. Use JPEG, PNG or WebP.",
        )

    image_bytes = await file.read()

    if len(image_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="Image too large. Maximum size is 10 MB.")

    result = ml_service.predict(image_bytes)

    if not result or "disease_key" not in result:
        raise HTTPException(status_code=500, detail="Prediction service returned an invalid result.")

    # Persist to history when user is authenticated
    if current_user:
        db = get_db()
        history_doc = {
            "user_email": current_user["sub"],
            "disease_key": result["disease_key"],
            "disease_name": result.get("name", result["disease_key"]),
            "crop": result.get("crop", ""),
            "confidence": result["confidence"],
            "severity": result.get("severity", "unknown"),
            "is_healthy": result.get("is_healthy", False),
            "image_filename": file.filename or "uploaded_image",
            "predicted_at": datetime.now(timezone.utc).isoformat(),
        }
        await db.predictions.insert_one(history_doc)

    treatment_raw = result.get("treatment", {})
    treatment = TreatmentInfo(
        organic=treatment_raw.get("organic", []),
        chemical=treatment_raw.get("chemical", []),
        dosage_per_acre=treatment_raw.get("dosage_per_acre"),
        indian_brands=treatment_raw.get("indian_brands", []),
    )

    return PredictResponse(
        disease_key=result["disease_key"],
        disease_name=result.get("name", result["disease_key"]),
        crop=result.get("crop", ""),
        confidence=result["confidence"],
        description=result.get("description", ""),
        symptoms=result.get("symptoms", []),
        treatment=treatment,
        prevention=result.get("prevention", []),
        severity=result.get("severity", "unknown"),
        is_healthy=result.get("is_healthy", False),
    )
