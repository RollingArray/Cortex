from fastapi import APIRouter

from backend.api.v1.endpoints import documents
from backend.api.v1.endpoints.health import router as health_router
from backend.api.v1.endpoints.chat import router as chat_router
from backend.api.v1.endpoints.knowledge import router as knowledge_router
from backend.api.v1.endpoints.retrieval import router as retrieval_router
from backend.api.v1.endpoints.rag import router as rag_router
from backend.api.v1.endpoints.workspace import router as workspace_router
from backend.api.v1.endpoints.documents import router as documents_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(knowledge_router)
api_router.include_router(retrieval_router)
api_router.include_router(chat_router)
api_router.include_router(rag_router)
api_router.include_router(workspace_router)
api_router.include_router(documents_router)
