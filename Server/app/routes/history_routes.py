"""
History routes — User prediction history
"""

from fastapi import APIRouter, Depends, Query
from app.auth import require_auth
from app.database import get_db

router = APIRouter(prefix="/api", tags=["History"])


@router.get("/history")
async def get_history(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    current_user=Depends(require_auth),
):
    """
    Get the current user's prediction history (paginated, newest first).
    Requires authentication.
    """
    db = get_db()
    user_id = current_user["_id"]

    skip = (page - 1) * limit

    # Count total
    total = await db.predictions.count_documents({"user_id": user_id})

    # Fetch predictions
    cursor = (
        db.predictions.find({"user_id": user_id})
        .sort("created_at", -1)
        .skip(skip)
        .limit(limit)
    )

    predictions = []
    async for doc in cursor:
        predictions.append(
            {
                "prediction_id": str(doc["_id"]),
                "crop_name": doc.get("crop_name", ""),
                "disease_name": doc.get("disease_name", ""),
                "confidence": doc.get("confidence", 0),
                "severity": doc.get("severity", ""),
                "status": doc.get("status", ""),
                "description": doc.get("description", ""),
                "organic_treatment": doc.get("organic_treatment", []),
                "chemical_treatment": doc.get("chemical_treatment", []),
                "dosage": doc.get("dosage", ""),
                "prevention": doc.get("prevention", []),
                "filename": doc.get("filename", ""),
                "created_at": doc.get("created_at", ""),
            }
        )

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "predictions": predictions,
    }
