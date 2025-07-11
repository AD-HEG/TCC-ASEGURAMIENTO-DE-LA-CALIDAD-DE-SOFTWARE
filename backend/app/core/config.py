from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl



class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    # JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    # REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7    # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "PricePulse"

    # Database
    MONGO_CONNECTION_STRING: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

print("Cargando MONGO_CONNECTION_STRING:", Settings().MONGO_CONNECTION_STRING)
