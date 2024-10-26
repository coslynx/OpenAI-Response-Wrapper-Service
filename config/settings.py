from pydantic import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path('.env'))

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.environ["OPENAI_API_KEY"]
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    JWT_SECRET_KEY: str = os.environ["JWT_SECRET_KEY"]
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")
    REDIS_HOST: str = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.environ.get("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.environ.get("REDIS_DB", 0))
    PORT: int = int(os.environ.get("PORT", 8000))

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()