import uuid

from backend.services.embeddings.factory import (
    get_embedding_provider,
)

from backend.services.vectorstores.factory import (
    get_vector_store,
)

from backend.services.vectorstores.models import (
    VectorRecord,
)


class IndexingService:

    async def index_text(
        self,
        text: str,
        source: str,
    ):

        embedding_provider = (
            get_embedding_provider()
        )

        vector_store = (
            get_vector_store()
        )

        embedding = (
            await embedding_provider.embed(
                text
            )
        )

        record = VectorRecord(
            id=str(uuid.uuid4()),
            content=text,
            embedding=embedding.vector,
            source=source,
        )

        await vector_store.add(
            record
        )

        return record