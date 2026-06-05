import pytest

from app.services.knowledge.indexing_service import (
    IndexingService,
)


@pytest.mark.asyncio
async def test_indexing():

    service = IndexingService()

    record = await service.index_text(
        text="Cortex Knowledge",
        source="test",
    )

    assert record.content == (
        "Cortex Knowledge"
    )