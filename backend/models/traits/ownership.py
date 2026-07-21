"""
Ownership Trait

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides ownership information for database
entities.

Features:
---------
- Created by
- Updated by
"""

# =============================================================================
# Imports
# =============================================================================

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.constants import PRINCIPAL_ID_LENGTH, UUID_LENGTH

# =============================================================================
# Ownable Trait
# =============================================================================


class Ownable:
    """
    Adds ownership information to an entity.
    """

    __abstract__ = True

    # -------------------------------------------------------------------------
    # Ownership Fields
    # -------------------------------------------------------------------------

    created_by: Mapped[str | None] = mapped_column(
        String(PRINCIPAL_ID_LENGTH),
        nullable=True,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String(PRINCIPAL_ID_LENGTH),
        nullable=True,
    )
