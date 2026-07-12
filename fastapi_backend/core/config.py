from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables / .env file.
    """
    DATABASE_URL: str = "sqlite:///./students.db"
    APP_NAME: str = "SEN 401 Lab 4 - Student API"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
