"""
Disease information routes
"""

from fastapi import APIRouter, HTTPException, Query
from app.services.disease_data import (
    get_disease_info,
    get_all_diseases,
    get_diseases_by_crop,
    DISEASE_DATABASE,
)

router = APIRouter(prefix="/api", tags=["Disease Info"])


@router.get("/diseases")
async def list_diseases(crop: str | None = Query(None, description="Filter by crop name")):
    """
    List all known diseases, optionally filtered by crop.
    """
    if crop:
        diseases = get_diseases_by_crop(crop)
    else:
        diseases = get_all_diseases()

    return {
        "total": len(diseases),
        "diseases": [
            {
                "class_key": d["class_key"],
                "disease_name": d["disease_name"],
                "crop": d["crop"],
                "severity": d["severity"],
            }
            for d in diseases
        ],
    }


@router.get("/diseases/{class_key}")
async def get_disease_detail(class_key: str):
    """
    Get full disease details including treatments, dosage, and prevention.
    """
    info = get_disease_info(class_key)
    if not info:
        raise HTTPException(status_code=404, detail=f"Disease '{class_key}' not found")
    return {**info, "class_key": class_key}


@router.get("/crops")
async def list_crops():
    """List all supported crops."""
    crops = sorted(set(v["crop"] for v in DISEASE_DATABASE.values()))
    return {"crops": crops}
