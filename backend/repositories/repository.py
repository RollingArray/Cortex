"""
Repository

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the common repository abstraction
used by all Cortex repositories.

Features:
---------
- Database session
- Shared repository foundation
"""

# =============================================================================
# Imports
# =============================================================================

from sqlalchemy.orm import Session

# =============================================================================
# Repository
# =============================================================================


class Repository:
    """
    Base repository.
    """

    def __init__(
        self,
        database: Session,
    ) -> None:

        self._database = database
