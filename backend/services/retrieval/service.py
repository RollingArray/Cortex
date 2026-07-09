from backend.services.embeddings.factory import (
    get_embedding_provider,
)

from backend.services.retrieval.models import (
    RetrievalResult,
)

from backend.services.vectorstores.factory import (
    get_vector_store,
)


class RetrievalService:

    async def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        embedding_provider = (
            get_embedding_provider()
        )

        vector_store = (
            get_vector_store()
        )

        query_embedding = (
            await embedding_provider.embed(
                query
            )
        )

        records = (
            await vector_store.search(
                query_embedding.vector,
                top_k,
            )
        )

        results = []

        for record in records:

            results.append(
                RetrievalResult(
                    id=record.id,
                    content=record.content,
                    source=record.source,
                )
            )

        return results