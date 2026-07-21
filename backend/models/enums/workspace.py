"""
Workspace Type Enumeration

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines supported workspace types
within the Cortex platform.

Features:
---------
- Personal workspaces
- Shared workspaces
"""

# =============================================================================
# Imports
# =============================================================================

from enum import Enum

# =============================================================================
# Workspace Type
# =============================================================================


class WorkspaceType(str, Enum):
    """
    Supported workspace types.
    """

    PERSONAL = "personal"

    SHARED = "shared"
