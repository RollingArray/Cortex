from backend.services.vectorstores.base import (
    VectorStore,
)


class MockVectorStore(
    VectorStore
):

    def __init__(self):

        self.records = []

    async def add(
        self,
        record,
    ) -> None:

        self.records.append(
            record
        )

    async def search(
        self,
        embedding,
        top_k=5,
    ):

        return self.records[:top_k]