from fastapi import APIRouter

from app.schemas.retrieval import (
    RetrievalRequest,
    RetrievalResponse,
)

from app.services.retrieval.service import (
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