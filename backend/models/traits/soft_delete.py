"""
Soft Delete Trait

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides soft deletion support for database
entities.

Features:
---------
- Deleted timestamp
- Deleted by
"""

# =============================================================================
# Imports
# =============================================================================

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.constants import PRINCIPAL_ID_LENGTH, UUID_LENGTH

# =============================================================================
# Soft Delete Trait
# =============================================================================


class SoftDeletable:
    """
    Adds soft deletion capability to an entity.
    """

    __abstract__ = True

    # -------------------------------------------------------------------------
    # Soft Delete Fields
    # -------------------------------------------------------------------------

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    deleted_by: Mapped[str | None] = mapped_column(
        String(PRINCIPAL_ID_LENGTH),
        nullable=True,
    )
