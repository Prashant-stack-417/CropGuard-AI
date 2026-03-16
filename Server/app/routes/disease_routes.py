from fastapi import APIRouter, HTTPException

from ..models import DiseaseListItem, DiseaseDetail
from ..services.disease_data import get_all_diseases, get_disease, get_crops

router = APIRouter(tags=["diseases"])


@router.get("/diseases", response_model=list[DiseaseListItem])
async def list_diseases():
    return get_all_diseases()


@router.get("/diseases/{key}", response_model=DiseaseDetail)
async def disease_detail(key: str):
    data = get_disease(key)
    if data is None:
        raise HTTPException(status_code=404, detail=f"Disease '{key}' not found")
    return data


@router.get("/crops", response_model=list[str])
async def list_crops():
    return get_crops()
