import pytest

from app.services.pipelines.indexing_pipeline import (
    KnowledgeIndexingPipeline,
)


@pytest.mark.asyncio
async def test_pipeline():

    pipeline = (
        KnowledgeIndexingPipeline()
    )

    result = (
        await pipeline.index_document(
            "data/sample/cortex.txt"
        )
    )

    assert (
        result.indexed_records > 0
    )