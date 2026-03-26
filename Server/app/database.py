"""
MongoDB connection using Motor (async driver).
"""

import logging

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException, status
from app.config import MONGODB_URI, DATABASE_NAME

client: AsyncIOMotorClient = None
db = None
logger = logging.getLogger("cropguard.db")


async def connect_db():
    """Open MongoDB connection. Returns True if connected, False otherwise."""
    global client, db
    try:
        client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=3000)
        await client.admin.command("ping")
        db = client[DATABASE_NAME]

        # Create indexes
        await db.users.create_index("email", unique=True)
        await db.predictions.create_index("user_id")
        await db.predictions.create_index("created_at")
        await db.diseases.create_index("disease_name", unique=True)

        logger.info(f"Connected to MongoDB: {DATABASE_NAME}")
        return True
    except Exception as e:
        logger.warning(f"MongoDB unavailable, continuing in stateless mode: {e}")
        client = None
        db = None
        return False


async def close_db():
    """Close MongoDB connection."""
    global client
    if client:
        client.close()
        print("🔌 MongoDB connection closed")


def get_db():
    """Return the database instance."""
    if db is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is not configured or currently unavailable.",
        )
    return db


def is_db_connected() -> bool:
    return db is not None
