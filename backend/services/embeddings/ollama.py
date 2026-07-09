from ollama import AsyncClient

from backend.core.config import settings
from backend.services.embeddings.base import (
    EmbeddingProvider,
)
from backend.services.embeddings.models import (
    Embedding,
)


class OllamaEmbeddingProvider(
    EmbeddingProvider
):

    def __init__(self):

        self.client = AsyncClient(
            host=settings.ollama_host,
        )

    async def embed(
        self,
        text: str,
    ) -> Embedding:

        response = await self.client.embed(
            model=settings.ollama_embedding_model,
            input=text,
        )

        vector = response["embeddings"][0]

        return Embedding(
            vector=vector,
            dimensions=len(vector),
        )