from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import get_logger

router = APIRouter(tags=["Health"])

@router.get("/health")
async def health():
    logger = get_logger(__name__)
    logger.info("Health endpoint invoked")

    return {
        "status": "healthy"
    }


@router.get("/ready")
async def readiness():
    logger = get_logger(__name__)
    logger.info("Readiness endpoint invoked")

    return {
        "status": "ready"
    }


@router.get("/info")
async def info():
    logger = get_logger(__name__)
    logger.info("Info endpoint invoked")

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment.value,
    }