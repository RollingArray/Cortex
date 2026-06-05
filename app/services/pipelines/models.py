from dataclasses import dataclass


@dataclass
class IndexingResult:
    source: str
    chunk_count: int
    indexed_records: int