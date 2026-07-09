from dataclasses import dataclass
from typing import Any

@dataclass
class VectorRecord:
    id: str
    content: str
    embedding: list[float]
    source: str
    metadata: dict[str, Any] | None = None