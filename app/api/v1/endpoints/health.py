from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import get_logger
from app.schemas.health import (
    HealthResponse,
    ReadinessResponse,
    ServiceInfoResponse,
)
from app.exceptions.custom import CortexException

router = APIRouter(tags=["Health"])

@router.get(
    "/health",
    response_model=HealthResponse,
)
async def health():
    logger = get_logger(__name__)
    logger.info("Health endpoint invoked")

    return {
        "status": "healthy"
    }


@router.get(
        "/ready",
        response_model=ReadinessResponse,
)
async def readiness():
    logger = get_logger(__name__)
    logger.info("Readiness endpoint invoked")

    return {
        "status": "ready"
    }


@router.get(
    "/info",
    response_model=ServiceInfoResponse,
)
async def info():
    logger = get_logger(__name__)
    logger.info("Info endpoint invoked")

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment.value,
    }

@router.get("/error")
async def error():

    raise CortexException(
        message="Intentional test error",
        code="TEST_ERROR",
    )