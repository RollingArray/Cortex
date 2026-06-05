from abc import ABC
from abc import abstractmethod

from app.services.embeddings.models import (
    Embedding,
)


class EmbeddingProvider(ABC):

    @abstractmethod
    async def embed(
        self,
        text: str,
    ) -> Embedding:
        pass