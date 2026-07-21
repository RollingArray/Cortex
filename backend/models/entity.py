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

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.base import Base

from uuid import UUID, uuid4

from sqlalchemy import Uuid

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

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4,
    )
