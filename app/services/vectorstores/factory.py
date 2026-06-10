from functools import lru_cache

from app.core.config import (
    VectorStoreProvider,
    settings,
)
from app.services.vectorstores.mock import (
    MockVectorStore,
)
from app.services.vectorstores.qdrant import (
    QdrantVectorStore,
)


@lru_cache
def get_vector_store():

    match settings.vector_store_provider:

        case VectorStoreProvider.MOCK:
            return MockVectorStore()

        case VectorStoreProvider.QDRANT:
            return QdrantVectorStore()

        case _:
            raise ValueError(
                (
                    "Unsupported vector store provider: "
                    f"{settings.vector_store_provider}"
                )
            )