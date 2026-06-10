from app.services.ai.factory import (
    get_ai_provider,
)

from app.services.embeddings.factory import (
    get_embedding_provider,
)

from app.services.vectorstores.factory import (
    get_vector_store,
)


class RAGService:

    async def ask(
        self,
        question: str,
    ):

        embedding_provider = (
            get_embedding_provider()
        )

        vector_store = (
            get_vector_store()
        )

        ai_provider = (
            get_ai_provider()
        )

        query_embedding = (
            await embedding_provider.embed(
                question
            )
        )

        records = await vector_store.search(
            embedding=query_embedding.vector,
            top_k=5,
        )

        context = "\n\n".join(
            record.content
            for record in records
        )

        prompt = f"""
Use the provided context to answer
the question.

If the answer cannot be found in
the context, say so clearly.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = (
            await ai_provider.generate(
                prompt
            )
        )

        return {
            "answer": answer,
            "retrieved_chunks": [
                record.content
                for record in records
            ],
        }