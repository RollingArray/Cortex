"""
Database Base Model

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the declarative base for all SQLAlchemy
database models used by the Cortex platform.

Features:
---------
- Declarative model base
- Common metadata
- Enterprise naming conventions
"""

# =============================================================================
# Imports
# =============================================================================

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# =============================================================================
# Database Naming Convention
# =============================================================================

NAMING_CONVENTION = {
    # -------------------------------------------------------------------------
    # Indexes
    # -------------------------------------------------------------------------
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    # -------------------------------------------------------------------------
    # Unique Constraints
    # Explicitly named in model definitions.
    # -------------------------------------------------------------------------
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    # -------------------------------------------------------------------------
    # Check Constraints
    # Explicitly named in model definitions.
    # -------------------------------------------------------------------------
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # -------------------------------------------------------------------------
    # Foreign Keys
    # -------------------------------------------------------------------------
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    # -------------------------------------------------------------------------
    # Primary Keys
    # -------------------------------------------------------------------------
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(
    naming_convention=NAMING_CONVENTION,
)

# =============================================================================
# Declarative Base
# =============================================================================


class Base(DeclarativeBase):
    """
    Base class for all Cortex database models.
    """

    metadata = metadata
