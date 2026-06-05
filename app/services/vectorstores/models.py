from dataclasses import dataclass


@dataclass
class VectorRecord:
    id: str
    content: str
    embedding: list[float]
    source: str