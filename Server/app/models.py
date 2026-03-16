from typing import Any, Optional
from pydantic import BaseModel, EmailStr, field_validator


# ---------- Auth ----------

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_min_length(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters")
        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- Prediction ----------

class TreatmentInfo(BaseModel):
    organic: list[str]
    chemical: list[str]
    dosage_per_acre: Optional[str] = None
    indian_brands: list[str] = []


class PredictResponse(BaseModel):
    disease_key: str
    disease_name: str
    crop: str
    confidence: float
    description: str
    symptoms: list[str]
    treatment: TreatmentInfo
    prevention: list[str]
    severity: str
    is_healthy: bool


# ---------- History ----------

class HistoryItem(BaseModel):
    id: str
    disease_key: str
    disease_name: str
    crop: str
    confidence: float
    severity: str
    is_healthy: bool
    image_filename: str
    predicted_at: str


# ---------- Disease catalogue ----------

class DiseaseListItem(BaseModel):
    key: str
    name: str
    crop: str
    severity: str
    is_healthy: bool


class DiseaseDetail(BaseModel):
    key: str
    name: str
    crop: str
    description: str
    symptoms: list[str]
    treatment: dict[str, Any]
    prevention: list[str]
    severity: str
    is_healthy: bool
