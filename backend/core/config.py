import os
from enum import Enum
from functools import lru_cache
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict

# ==================================================
# Environment Configuration
# ==================================================


class Environment(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


# ==================================================
# AI Providers
# ==================================================


class AIProvider(str, Enum):
    MOCK = "mock"
    OLLAMA = "ollama"


# ==================================================
# Embedding Providers
# ==================================================


class EmbeddingProvider(str, Enum):
    MOCK = "mock"
    OLLAMA = "ollama"


# ==================================================
# Runtime Environment
# ==================================================

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    Environment.LOCAL.value,
)


class VectorStoreProvider(str, Enum):
    MOCK = "mock"
    QDRANT = "qdrant"


# ==================================================
# Database Providers
# ==================================================


class DatabaseProvider(str, Enum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"


# ==================================================
# Application Settings
# ==================================================


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
    # CORS Configuration
    # --------------------------------------------------

    cors_allowed_origins: list[str] = Field(
        default_factory=lambda: [
            "http://localhost:8100",
            "http://localhost:8101",
        ]
    )

    # --------------------------------------------------
    # AI Configuration
    # --------------------------------------------------

    ai_provider: AIProvider = AIProvider.MOCK

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # --------------------------------------------------
    # Embedding Configuration
    # --------------------------------------------------

    embedding_provider: EmbeddingProvider = EmbeddingProvider.MOCK

    ollama_embedding_model: str = "nomic-embed-text"

    # --------------------------------------------------
    # Vector Store Configuration
    # --------------------------------------------------

    vector_store_provider: VectorStoreProvider = VectorStoreProvider.MOCK

    qdrant_mode: str = "memory"

    qdrant_path: str = "data/qdrant"

    qdrant_collection_name: str = "cortex_knowledge"
    # --------------------------------------------------
    # Pydantic Settings
    # --------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=f"configs/environments/{ENVIRONMENT}.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --------------------------------------------------
    # Database Configuration
    # --------------------------------------------------

    database_provider: DatabaseProvider = DatabaseProvider.SQLITE

    database_url: str


@lru_cache
def get_settings() -> "Settings":
    """
    Returns a cached Settings instance.

    Settings are loaded once during application startup
    and reused throughout the application lifecycle.
    """

    return Settings()


settings = get_settings()
