from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings):
    CORS_ORIGINS: list[str] = ["http://localhost", "http://localhost:3000"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]
    DATABASE_URL: PostgresDsn

    class Config:
        env_file = ".env"

settings = Settings()