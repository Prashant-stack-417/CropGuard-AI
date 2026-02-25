"""
Pydantic schemas for request/response validation.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


# ── Auth ──────────────────────────────────────────────────────────────
class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    token: str
    user: dict


# ── Disease & Treatment ──────────────────────────────────────────────
class TreatmentInfo(BaseModel):
    organic: List[str]
    chemical: List[str]
    dosage: str
    application_method: str = ""


class DiseaseDocument(BaseModel):
    disease_name: str
    crop: str
    symptoms: List[str]
    cause: str
    description: str
    severity: str  # Low / Medium / High
    organic_treatment: List[str]
    chemical_treatment: List[str]
    dosage: str
    prevention: List[str]
    spread_risk: str  # Low / Medium / High


# ── Prediction ────────────────────────────────────────────────────────
class PredictionResponse(BaseModel):
    prediction_id: Optional[str] = None
    crop_name: str
    disease_name: str
    confidence: int
    severity: str
    spread_risk: str
    description: str
    symptoms: List[str]
    organic_treatment: List[str]
    chemical_treatment: List[str]
    dosage: str
    prevention: List[str]
    status: str  # Healthy / Diseased
    created_at: Optional[datetime] = None


# ── History ───────────────────────────────────────────────────────────
class HistoryItem(BaseModel):
    prediction_id: str
    crop_name: str
    disease_name: str
    confidence: int
    severity: str
    status: str
    created_at: datetime


class HistoryResponse(BaseModel):
    total: int
    predictions: List[HistoryItem]
