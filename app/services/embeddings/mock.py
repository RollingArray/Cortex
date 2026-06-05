from app.services.embeddings.base import (
    EmbeddingProvider,
)

from app.services.embeddings.models import (
    Embedding,
)


class MockEmbeddingProvider(
    EmbeddingProvider
):

    async def embed(
        self,
        text: str,
    ) -> Embedding:

        vector = [
            float(len(text)),
            float(len(text) / 2),
            float(len(text) / 4),
        ]

        return Embedding(
            vector=vector,
            dimensions=len(vector),
        )