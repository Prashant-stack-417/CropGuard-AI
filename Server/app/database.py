from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

_client: AsyncIOMotorClient | None = None


async def connect_db():
    global _client
    _client = AsyncIOMotorClient(settings.MONGO_URI)


async def close_db():
    global _client
    if _client:
        _client.close()
        _client = None


def get_db():
    if _client is None:
        raise RuntimeError("Database not connected. Call connect_db() first.")
    return _client[settings.DB_NAME]
