from app.services.ai.factory import (
    get_ai_provider,
)


class ChatService:

    async def generate_response(
        self,
        prompt: str,
    ) -> str:

        provider = get_ai_provider()

        return await provider.generate(
            prompt
        )