"""
CORS Configuration

Author:
-------
Ranjoy Sen

Purpose:
--------
Configures Cross-Origin Resource Sharing (CORS)
for the Cortex application.

Responsibilities:
-----------------
- Register CORS middleware
- Configure allowed origins
"""

# ==============================================================================
# Imports
# ==============================================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import settings

# ==============================================================================
# Public Functions
# ==============================================================================


def configure_cors(app: FastAPI) -> None:
    """
    Register the application's CORS middleware.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )