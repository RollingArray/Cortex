from fastapi import APIRouter

from backend.core.logging import get_logger
from backend.schemas.knowledge import (
    KnowledgeIndexRequest,
    KnowledgeIndexResponse,
)
from backend.services.pipelines.indexing_pipeline import (
    KnowledgeIndexingPipeline,
)

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"],
)

logger = get_logger(__name__)


@router.post(
    "/index",
    response_model=KnowledgeIndexResponse,
)
async def index_document(
    request: KnowledgeIndexRequest,
):

    logger.info(
        "Indexing document: %s",
        request.path,
    )

    pipeline = KnowledgeIndexingPipeline()

    result = await pipeline.index_document(
        request.path,
    )

    return KnowledgeIndexResponse(
        source=result.source,
        chunk_count=result.chunk_count,
        indexed_records=result.indexed_records,
    )