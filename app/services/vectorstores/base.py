from abc import ABC
from abc import abstractmethod

from app.services.vectorstores.models import (
    VectorRecord,
)


class VectorStore(ABC):

    @abstractmethod
    async def add(
        self,
        record: VectorRecord,
    ) -> None:
        pass

    @abstractmethod
    async def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ):
        pass