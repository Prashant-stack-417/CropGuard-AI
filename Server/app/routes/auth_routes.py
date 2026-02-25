"""
Authentication routes — Register & Login
"""

from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status
from app.database import get_db
from app.auth import hash_password, verify_password, create_access_token
from app.models import RegisterRequest, LoginRequest, AuthResponse

router = APIRouter(prefix="/api", tags=["Authentication"])


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(req: RegisterRequest):
    """Register a new user."""
    db = get_db()

    # Check if email already exists
    existing = await db.users.find_one({"email": req.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists",
        )

    # Create user document
    user_doc = {
        "name": req.name,
        "email": req.email,
        "password_hash": hash_password(req.password),
        "role": "farmer",
        "created_at": datetime.now(timezone.utc),
    }

    result = await db.users.insert_one(user_doc)
    user_id = str(result.inserted_id)

    token = create_access_token(user_id, req.email, req.name)

    return AuthResponse(
        token=token,
        user={
            "id": user_id,
            "name": req.name,
            "email": req.email,
            "role": "farmer",
        },
    )


@router.post("/login", response_model=AuthResponse)
async def login(req: LoginRequest):
    """Login and get a JWT token."""
    db = get_db()

    user = await db.users.find_one({"email": req.email})
    if not user or not verify_password(req.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    user_id = str(user["_id"])
    token = create_access_token(user_id, user["email"], user["name"])

    return AuthResponse(
        token=token,
        user={
            "id": user_id,
            "name": user["name"],
            "email": user["email"],
            "role": user.get("role", "farmer"),
        },
    )
