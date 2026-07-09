from backend.services.chunking.base import Chunker
from backend.services.chunking.models import (
    DocumentChunk,
)
from backend.services.documents.models import (
    Document,
)


class CharacterChunker(
    Chunker
):

    def __init__(
        self,
        chunk_size: int = 500,
    ):
        self.chunk_size = chunk_size

    def chunk(
        self,
        document: Document,
    ):

        chunks = []

        text = document.content

        for index, start in enumerate(
            range(
                0,
                len(text),
                self.chunk_size,
            )
        ):

            end = (
                start
                + self.chunk_size
            )

            chunk_text = text[
                start:end
            ]

            chunks.append(
                DocumentChunk(
                    content=chunk_text,
                    chunk_index=index,
                    source=document.source,
                )
            )

        return chunks