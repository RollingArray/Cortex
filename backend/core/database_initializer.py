"""
Database Initializer

Author:
-------
Ranjoy Sen

Purpose:
--------
Creates the Cortex database schema during
application startup.

Notes
-----
This module is intended for local development.

Production deployments should use Alembic
database migrations.
"""

# =============================================================================
# Imports
# =============================================================================

import backend.models

from backend.core.database import engine
from backend.models import Base

# =============================================================================
# Public Functions
# =============================================================================


def initialize_database() -> None:
    """
    Create all database tables.

    Safe to execute multiple times.
    """

    Base.metadata.create_all(bind=engine)
