from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.ai.factory import (
    get_ai_provider,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):

    provider = get_ai_provider()

    response = await provider.generate(
        request.prompt
    )

    return ChatResponse(
        response=response
    )