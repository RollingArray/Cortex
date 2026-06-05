from pydantic import BaseModel


class RetrievalRequest(BaseModel):
    query: str


class RetrievalResponse(BaseModel):
    success: bool = True
    results: list[str]