from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId

from ..auth import get_current_user
from ..database import get_db
from ..models import HistoryItem

router = APIRouter(tags=["history"])


def _doc_to_item(doc: dict) -> HistoryItem:
    return HistoryItem(
        id=str(doc["_id"]),
        disease_key=doc["disease_key"],
        disease_name=doc["disease_name"],
        crop=doc["crop"],
        confidence=doc["confidence"],
        severity=doc["severity"],
        is_healthy=doc["is_healthy"],
        image_filename=doc["image_filename"],
        predicted_at=doc["predicted_at"],
    )


@router.get("/history", response_model=list[HistoryItem])
async def get_history(current_user: dict = Depends(get_current_user)):
    db = get_db()
    cursor = db.predictions.find(
        {"user_email": current_user["sub"]},
        sort=[("predicted_at", -1)],
    )
    docs = await cursor.to_list(length=100)
    return [_doc_to_item(d) for d in docs]


@router.delete("/history/{item_id}", status_code=204)
async def delete_history_item(
    item_id: str,
    current_user: dict = Depends(get_current_user),
):
    db = get_db()
    try:
        oid = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=422, detail="Invalid item ID format")

    result = await db.predictions.delete_one(
        {"_id": oid, "user_email": current_user["sub"]}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="History item not found")
