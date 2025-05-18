from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    DATABASE_URL: str
    MAX_TEXT_LENGTH: int = 10000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()