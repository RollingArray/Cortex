from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.ai.factory import (
    get_ai_provider,
)

from app.services.chat.service import (
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