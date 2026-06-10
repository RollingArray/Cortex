from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    retrieved_chunks: list[str]