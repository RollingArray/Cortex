from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.core.config import settings
from app.services.vectorstores.base import (
    VectorStore,
)
from app.services.vectorstores.models import (
    VectorRecord,
)
from pathlib import Path


class QdrantVectorStore(
    VectorStore
):

    def __init__(self):

        Path(
            settings.qdrant_path
        ).mkdir(
            parents=True,
            exist_ok=True,
        )

        if settings.qdrant_mode == "memory":

            self.client = QdrantClient(
                ":memory:"
            )

        else:

            self.client = QdrantClient(
                path=settings.qdrant_path
            )

        self.collection_name = (
            settings.qdrant_collection_name
        )

        self._initialized = False

    def _ensure_collection(
        self,
        dimensions: int,
    ):

        if self._initialized:
            return

        if not self.client.collection_exists(
            self.collection_name
        ):

            self.client.create_collection(
                collection_name=(
                    self.collection_name
                ),
                vectors_config=VectorParams(
                    size=dimensions,
                    distance=Distance.COSINE,
                ),
            )

        self._initialized = True

    async def add(
        self,
        record: VectorRecord,
    ) -> None:

        self._ensure_collection(
            len(record.embedding)
        )

        self.client.upsert(
            collection_name=(
                self.collection_name
            ),
            points=[
                PointStruct(
                    id=record.id,
                    vector=record.embedding,
                    payload={
                        "content": record.content,
                        "source": record.source,
                    },
                )
            ],
        )

    async def search(
        self,
        embedding,
        top_k=5,
    ):

        response = self.client.query_points(
            collection_name=self.collection_name,
            query=embedding,
            limit=top_k,
        )

        records = []

        for point in response.points:

            payload = point.payload

            records.append(
                VectorRecord(
                    id=str(point.id),
                    content=payload["content"],
                    embedding=[],
                    source=payload["source"],
                )
            )

        return records