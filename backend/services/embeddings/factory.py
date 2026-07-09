from backend.core.config import settings

from backend.services.embeddings.mock import (
    MockEmbeddingProvider,
)

from backend.services.embeddings.ollama import (
    OllamaEmbeddingProvider,
)


def get_embedding_provider():

    match settings.embedding_provider:

        case "mock":
            return MockEmbeddingProvider()

        case "ollama":
            return OllamaEmbeddingProvider()

        case _:
            raise ValueError(
                (
                    "Unsupported embedding "
                    f"provider: "
                    f"{settings.embedding_provider}"
                )
            )