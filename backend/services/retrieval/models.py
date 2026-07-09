from dataclasses import dataclass


@dataclass
class RetrievalResult:
    id: str
    content: str
    source: str