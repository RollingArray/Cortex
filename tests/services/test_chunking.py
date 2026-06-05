from app.services.chunking.character import (
    CharacterChunker,
)

from app.services.documents.models import (
    Document,
)


def test_character_chunking():

    document = Document(
        content="A" * 1200,
        source="test.txt",
    )

    chunker = CharacterChunker(
        chunk_size=500
    )

    chunks = chunker.chunk(
        document
    )

    assert len(chunks) == 3