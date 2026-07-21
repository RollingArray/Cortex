"""
Database Entity Traits

Author:
-------
Ranjoy Sen

Purpose:
--------
Exports reusable traits that provide common
capabilities to Cortex database entities.
"""

from backend.models.traits.audit import Auditable
from backend.models.traits.ownership import Ownable
from backend.models.traits.soft_delete import SoftDeletable

__all__ = [
    "Auditable",
    "Ownable",
    "SoftDeletable",
]
