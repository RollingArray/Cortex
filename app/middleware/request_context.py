import time
import uuid

from fastapi import Request

from app.core.logging import get_logger


async def request_context_middleware(
    request: Request,
    call_next,
):
    request_id = str(uuid.uuid4())

    start_time = time.time()

    response = await call_next(request)

    duration = round(
        time.time() - start_time,
        4,
    )

    logger = get_logger(__name__)
    logger.info(
        (
            "request_id=%s "
            "method=%s "
            "path=%s "
            "status_code=%s "
            "duration=%ss"
        ),
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    response.headers["X-Request-ID"] = request_id

    return response