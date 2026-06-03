import os
from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


class AIProvider(str, Enum):
    MOCK = "mock"
    OLLAMA = "ollama"


ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    Environment.LOCAL.value,
)


class Settings(BaseSettings):
    """
    Cortex application settings.

    Values are loaded from:

    configs/environments/{ENVIRONMENT}.env
    """

    # --------------------------------------------------
    # Application Metadata
    # --------------------------------------------------

    app_name: str
    app_version: str

    # --------------------------------------------------
    # Runtime Environment
    # --------------------------------------------------

    environment: Environment

    debug: bool = False
    log_level: str = "INFO"

    # --------------------------------------------------
    # AI Configuration
    # --------------------------------------------------

    ai_provider: AIProvider = AIProvider.MOCK

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # --------------------------------------------------
    # Pydantic Settings
    # --------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=f"configs/environments/{ENVIRONMENT}.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> "Settings":
    """
    Returns a cached Settings instance.

    Settings are loaded once during application startup
    and reused throughout the application lifecycle.
    """

    return Settings()


settings = get_settings()