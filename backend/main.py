from fastapi import FastAPI
from backend.core.cors import configure_cors

from backend.api.v1.router import api_router
from backend.core.config import settings
from backend.core.logging import configure_logging, get_logger
from backend.exceptions.custom import CortexException
from backend.exceptions.handlers import (
    cortex_exception_handler,
    generic_exception_handler,
)
from backend.middleware.request_context import (
    request_context_middleware,
)

configure_logging()

logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="AI-powered knowledge and reasoning platform",
    version=settings.app_version,
)

configure_cors(app)

app.middleware("http")(
    request_context_middleware
)
app.add_exception_handler(
    CortexException,
    cortex_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    logger.info(
        "Cortex application started | environment=%s",
        settings.environment.value,
    )


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }