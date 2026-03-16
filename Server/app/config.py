from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "cropguard"
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    MODEL_PATH: str = "model/crop_disease_model.pt"
    CLASS_MAP_PATH: str = "model/class_map.json"

    class Config:
        env_file = ".env"


settings = Settings()
