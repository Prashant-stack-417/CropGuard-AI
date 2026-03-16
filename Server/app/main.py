from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import connect_db, close_db
from .routes.auth_routes import router as auth_router
from .routes.predict_routes import router as predict_router
from .routes.history_routes import router as history_router
from .routes.disease_routes import router as disease_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()


app = FastAPI(
    title="CropGuard API",
    description="AI-powered crop disease detection for Indian agriculture",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(predict_router, prefix="/api")
app.include_router(history_router, prefix="/api")
app.include_router(disease_router, prefix="/api")


@app.get("/", tags=["health"])
async def health_check():
    return {"status": "ok", "service": "CropGuard API"}
