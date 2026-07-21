import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from backend.exceptions.custom import CortexException
from backend.schemas.error import ErrorDetail, ErrorResponse


async def cortex_exception_handler(
    request: Request,
    exc: CortexException,
):
    logger = logging.getLogger(__name__)
    logger.error(
        "Cortex exception: %s",
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=ErrorDetail(
                code=exc.code,
                message=exc.message,
            )
        ).model_dump(),
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    logger = logging.getLogger(__name__)
    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="An unexpected error occurred",
            )
        ).model_dump(),
    )
