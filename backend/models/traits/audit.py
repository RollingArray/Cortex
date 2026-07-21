"""
Audit Trait

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides audit timestamps for database entities.

Features:
---------
- Created timestamp
- Updated timestamp
"""

# =============================================================================
# Imports
# =============================================================================

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# =============================================================================
# Auditable Trait
# =============================================================================


class Auditable:
    """
    Adds audit information to an entity.
    """

    __abstract__ = True

    # -------------------------------------------------------------------------
    # Audit Fields
    # -------------------------------------------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
