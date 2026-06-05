from app.services.embeddings.factory import (
    get_embedding_provider,
)


class EmbeddingService:

    async def generate_embedding(
        self,
        text: str,
    ):

        provider = (
            get_embedding_provider()
        )

        return await provider.embed(
            text
        )