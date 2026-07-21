"""
Database Configuration

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides SQLAlchemy engine and session
configuration for the Cortex platform.

Responsibilities
----------------
- Create database engine
- Configure session factory
- Provide database dependency

This module intentionally performs no
database initialization.
"""

# =============================================================================
# Imports
# =============================================================================

from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

# =============================================================================
# SQLite Development
# =============================================================================

if settings.database_provider.value == "sqlite":
    Path("data").mkdir(exist_ok=True)

# =============================================================================
# Engine
# =============================================================================

engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    connect_args=(
        {"check_same_thread": False}
        if settings.database_provider.value == "sqlite"
        else {}
    ),
)

# =============================================================================
# Session Factory
# =============================================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

# =============================================================================
# Dependency
# =============================================================================


def get_database() -> Generator[Session, None, None]:
    """
    FastAPI database dependency.
    """

    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()
