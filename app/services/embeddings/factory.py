from app.services.embeddings.mock import (
    MockEmbeddingProvider,
)


def get_embedding_provider():

    return MockEmbeddingProvider()