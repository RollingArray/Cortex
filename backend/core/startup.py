"""
Application Startup

Author:
-------
Ranjoy Sen

Purpose:
--------
Coordinates all Cortex startup activities.

Responsibilities
----------------
- Initialize database
- Validate configuration
- Log startup information

Future
------
- Initialize vector databases
- Register AI providers
- Warm embedding models
- Start background workers
"""

# =============================================================================
# Imports
# =============================================================================

from backend.core.config import settings
from backend.core.database_initializer import initialize_database
from backend.core.logging import get_logger

logger = get_logger(__name__)

# =============================================================================
# Startup
# =============================================================================


def initialize_application() -> None:
    """
    Initialize Cortex application.
    """

    logger.info("Initializing Cortex...")

    initialize_database()

    logger.info(
        "Cortex initialized | environment=%s",
        settings.environment.value,
    )
