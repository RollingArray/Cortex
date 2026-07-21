"""
Workspace Repository

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides data access operations for
Workspace entities.

Features:
---------
- Retrieve personal workspace
- Retrieve workspace by id
- Retrieve workspace by name
- Persist workspace
- Delete workspace
"""

# =============================================================================
# Imports
# =============================================================================

from uuid import UUID

from sqlalchemy import select

from backend.models import Workspace
from backend.models.enums import WorkspaceType
from backend.repositories.repository import Repository

# =============================================================================
# Repository
# =============================================================================


class WorkspaceRepository(
    Repository,
):
    """
    Repository for Workspace entities.
    """

    # -------------------------------------------------------------------------
    # Queries
    # -------------------------------------------------------------------------

    def get_personal(
        self,
    ) -> Workspace | None:
        """
        Retrieve the default personal workspace.
        """

        statement = select(
            Workspace,
        ).where(
            Workspace.workspace_type == WorkspaceType.PERSONAL,
        )

        return self._database.scalar(
            statement,
        )

    def get_all(
        self,
    ) -> list[Workspace]:
        """
        Retrieve all workspaces.
        """

        statement = select(
            Workspace,
        ).order_by(
            Workspace.name,
        )

        return list(
            self._database.scalars(
                statement,
            ).all()
        )

    def get_by_id(
        self,
        workspace_id: UUID,
    ) -> Workspace | None:
        """
        Retrieve workspace by identifier.
        """

        statement = select(
            Workspace,
        ).where(
            Workspace.id == workspace_id,
        )

        return self._database.scalar(
            statement,
        )

    def get_by_name(
        self,
        name: str,
    ) -> Workspace | None:
        """
        Retrieve a workspace by name.
        """

        statement = select(
            Workspace,
        ).where(
            Workspace.name == name,
        )

        return self._database.scalar(
            statement,
        )

    # -------------------------------------------------------------------------
    # Commands
    # -------------------------------------------------------------------------

    def save(
        self,
        workspace: Workspace,
    ) -> Workspace:
        """
        Persist a workspace.
        """

        self._database.add(
            workspace,
        )

        self._database.commit()

        self._database.refresh(
            workspace,
        )

        return workspace

    def delete(
        self,
        workspace: Workspace,
    ) -> None:
        """
        Delete a workspace.
        """

        self._database.delete(
            workspace,
        )

        self._database.commit()
