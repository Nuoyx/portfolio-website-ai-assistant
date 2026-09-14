from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Portfolio AI Assistant"

    environment: str = "development"

    gemini_api_key: str

    gemini_model: str = "gemini-3.6-flash"

    redis_url: str = "redis://localhost:6379"

    redis_ttl_seconds: int = 86400

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def get_settings() -> Settings:
    return Settings()

