"""
Workspace Seeder

Author:
-------
Ranjoy Sen

Purpose:
--------
Seeds the default Workspace for
the Cortex platform.

Features:
---------
- Create Personal Workspace
"""

# =============================================================================
# Imports
# =============================================================================

from backend.core.database import (
    SessionLocal,
)

from backend.services.workspace import (
    WorkspaceService,
)

# =============================================================================
# Seeder
# =============================================================================


def seed_workspace() -> None:
    """
    Seed the default Personal Workspace.
    """

    database = SessionLocal()

    try:

        service = WorkspaceService(
            database,
        )

        workspace = service.create_personal_workspace()

        print()

        print(
            f"✓ Workspace '{workspace.name}' is ready.",
        )

    finally:

        database.close()
