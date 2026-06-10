import pytest

from app.services.embeddings.factory import (
    get_embedding_provider,
)


@pytest.mark.asyncio
async def test_ollama_embedding_generation():

    provider = get_embedding_provider()

    embedding = await provider.embed(
        "What is Cortex?"
    )

    assert embedding is not None

    assert embedding.dimensions > 0

    assert len(embedding.vector) == (
        embedding.dimensions
    )