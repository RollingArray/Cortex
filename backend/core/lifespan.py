"""
Application Lifespan

Author:
-------
Ranjoy Sen

Purpose:
--------
Manages application startup and shutdown.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.startup import initialize_application


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Cortex application lifecycle.
    """

    initialize_application()

    yield

    # Future shutdown logic
