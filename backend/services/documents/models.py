from pydantic import BaseModel


class Document:
    """
    Internal document representation.
    """

    def __init__(
        self,
        content: str,
        source: str,
    ):
        self.content = content
        self.source = source