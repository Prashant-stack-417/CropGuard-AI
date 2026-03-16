from fastapi import APIRouter, HTTPException, status

from ..database import get_db
from ..auth import hash_password, verify_password, create_access_token
from ..models import RegisterRequest, LoginRequest, TokenResponse

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest):
    db = get_db()
    if await db.users.find_one({"email": body.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user = {
        "name": body.name,
        "email": body.email,
        "password": hash_password(body.password),
    }
    await db.users.insert_one(user)
    token = create_access_token({"sub": body.email, "name": body.name})
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest):
    db = get_db()
    user = await db.users.find_one({"email": body.email})
    if not user or not verify_password(body.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": user["email"], "name": user.get("name", "")})
    return TokenResponse(access_token=token)
