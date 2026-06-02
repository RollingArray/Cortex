from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="AI-powered knowledge and reasoning platform",
    version=settings.app_version,
)


@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "environment": settings.environment,
    }