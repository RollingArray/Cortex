"""
Entity Base Model

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the common identity shared by all
Cortex database entities.

Features:
---------
- UUID primary key
"""

# =============================================================================
# Imports
# =============================================================================

from uuid import uuid4

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.base import Base
from backend.models.constants import UUID_LENGTH

# =============================================================================
# Entity Base
# =============================================================================


class Entity(Base):
    """
    Base entity inherited by all
    Cortex database models.

    Responsibilities
    ----------------
    - Unique identity
    """

    __abstract__ = True

    # -------------------------------------------------------------------------
    # Primary Key
    # -------------------------------------------------------------------------

    id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        primary_key=True,
        default=lambda: str(uuid4()),
    )
