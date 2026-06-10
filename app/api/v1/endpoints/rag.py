from fastapi import APIRouter

from app.services.rag.models import (
    AskRequest,
    AskResponse,
)

from app.services.rag.service import (
    RAGService,
)

router = APIRouter(
    prefix="/ask",
    tags=["RAG"],
)


@router.post(
    "",
    response_model=AskResponse,
)
async def ask(
    request: AskRequest,
):

    service = RAGService()

    result = await service.ask(
        request.question
    )

    return AskResponse(
        answer=result["answer"],
        retrieved_chunks=result[
            "retrieved_chunks"
        ],
    )