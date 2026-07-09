from pydantic import BaseModel

from backend.schemas.common import BaseResponse


class HealthResponse(BaseResponse):
    status: str


class ReadinessResponse(BaseResponse):
    status: str


class ServiceInfoResponse(BaseResponse):
    application: str
    version: str
    environment: str