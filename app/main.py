from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="AI-powered knowledge and reasoning platform",
    version=settings.app_version,
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }