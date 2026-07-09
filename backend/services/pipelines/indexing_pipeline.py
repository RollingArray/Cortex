from backend.services.chunking.character import (
    CharacterChunker,
)

from backend.services.documents.text_loader import (
    TextLoader,
)

from backend.services.knowledge.indexing_service import (
    IndexingService,
)

from backend.services.pipelines.models import (
    IndexingResult,
)


class KnowledgeIndexingPipeline:

    async def index_document(
        self,
        path: str,
    ) -> IndexingResult:

        loader = TextLoader()

        chunker = CharacterChunker()

        indexing_service = (
            IndexingService()
        )

        document = loader.load(path)

        chunks = chunker.chunk(
            document
        )

        indexed_records = 0

        for chunk in chunks:

            await indexing_service.index_text(
                text=chunk.content,
                source=chunk.source,
            )

            indexed_records += 1

        return IndexingResult(
            source=path,
            chunk_count=len(chunks),
            indexed_records=indexed_records,
        )