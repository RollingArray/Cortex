from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@router.get("/ready")
async def readiness():
    return {
        "status": "ready"
    }


@router.get("/info")
async def info():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment.value,
    }