import pytest

from app.services.knowledge.indexing_service import (
    IndexingService,
)
from app.services.retrieval.service import (
    RetrievalService,
)


@pytest.mark.asyncio
async def test_qdrant_retrieval():

    indexer = IndexingService()

    await indexer.index_text(
        text="Cortex is an AI-powered knowledge platform",
        source="test",
    )

    retrieval = RetrievalService()

    results = await retrieval.retrieve(
        "What is Cortex?"
    )

    assert len(results) > 0

    assert (
        "Cortex"
        in results[0].content
    )