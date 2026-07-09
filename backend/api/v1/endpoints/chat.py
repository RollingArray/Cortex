from fastapi import APIRouter

from backend.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from backend.services.ai.factory import (
    get_ai_provider,
)

from backend.services.chat.service import (
    ChatService,
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

    service = ChatService()

    response = await service.generate_response(
        request.prompt
    )

    return ChatResponse(
        response=response
    ) 