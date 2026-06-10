import pytest

from app.services.knowledge.indexing_service import (
    IndexingService,
)

from app.services.rag.service import (
    RAGService,
)


@pytest.mark.asyncio
async def test_rag_pipeline():

    indexer = IndexingService()

    await indexer.index_text(
        text=(
            "Cortex is an AI-powered "
            "knowledge platform."
        ),
        source="test",
    )

    rag = RAGService()

    result = await rag.ask(
        "What is Cortex?"
    )

    assert (
        len(result["answer"])
        > 0
    )

    assert (
        len(
            result["retrieved_chunks"]
        )
        > 0
    )