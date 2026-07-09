from pathlib import Path

from backend.services.documents.base import (
    DocumentLoader,
)
from backend.services.documents.models import (
    Document,
)


class TextLoader(
    DocumentLoader
):

    def load(
        self,
        path: str,
    ) -> Document:

        content = Path(
            path
        ).read_text(
            encoding="utf-8"
        )

        return Document(
            content=content,
            source=path,
        )