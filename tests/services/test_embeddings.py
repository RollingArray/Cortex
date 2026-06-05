import pytest

from app.services.knowledge.embedding_service import (
    EmbeddingService,
)


@pytest.mark.asyncio
async def test_embedding_generation():

    service = EmbeddingService()

    embedding = (
        await service.generate_embedding(
            "Cortex"
        )
    )

    assert embedding.dimensions == 3