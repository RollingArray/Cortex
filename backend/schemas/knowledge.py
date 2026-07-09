from pydantic import BaseModel


class KnowledgeIndexRequest(BaseModel):
    path: str


class KnowledgeIndexResponse(BaseModel):
    success: bool = True
    source: str
    chunk_count: int
    indexed_records: int