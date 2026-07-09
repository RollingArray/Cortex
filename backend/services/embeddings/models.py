from dataclasses import dataclass


@dataclass
class Embedding:
    vector: list[float]
    dimensions: int