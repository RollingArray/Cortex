from ollama import AsyncClient

from app.core.config import settings
from app.services.ai.base import AIProvider


class OllamaProvider(
    AIProvider
):
    """
    Ollama-based AI provider.
    """

    def __init__(self):

        self.client = AsyncClient(
            host=settings.ollama_host
        )

    async def generate(
        self,
        prompt: str,
    ) -> str:

        response = await self.client.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]