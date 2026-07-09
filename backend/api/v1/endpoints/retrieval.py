from fastapi import APIRouter

from backend.schemas.retrieval import (
    RetrievalRequest,
    RetrievalResponse,
)

from backend.services.retrieval.service import (
    RetrievalService,
)

router = APIRouter(
    prefix="/retrieve",
    tags=["Retrieval"],
)


@router.post(
    "",
    response_model=RetrievalResponse,
)
async def retrieve(
    request: RetrievalRequest,
):

    service = RetrievalService()

    results = await service.retrieve(
        request.query
    )

    return RetrievalResponse(
        results=[
            item.content
            for item in results
        ]
    )