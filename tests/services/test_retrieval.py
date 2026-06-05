import pytest

from app.services.knowledge.indexing_service import (
    IndexingService,
)

from app.services.retrieval.service import (
    RetrievalService,
)


@pytest.mark.asyncio
async def test_retrieval():

    indexer = IndexingService()

    await indexer.index_text(
        text="Cortex is an AI platform",
        source="test",
    )

    retrieval = RetrievalService()

    results = await retrieval.retrieve(
        query="What is Cortex?"
    )

    assert len(results) > 0