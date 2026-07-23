"""
Workspace Service

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides business operations for
Workspace resources.

Features:
---------
- List workspaces
- Retrieve workspace
- Create workspace
- Update workspace
- Delete workspace
- Bootstrap personal workspace
"""

# =============================================================================
# Imports
# =============================================================================

from uuid import UUID

from sqlalchemy.orm import Session

from backend.exceptions.already_exists import ResourceAlreadyExistsException
from backend.exceptions.resource import ResourceNotFoundException

from backend.models import Workspace
from backend.models.enums import WorkspaceType

from backend.repositories.workspace.repository import WorkspaceRepository

from backend.schemas.workspace import (
    WorkspaceSummary,
    CreateWorkspaceRequest,
    UpdateWorkspaceRequest,
)

from backend.services.base import (
    BaseService,
)

from backend.services.document.service import DocumentService
from backend.services.storage import StorageService

# =============================================================================
# Service
# =============================================================================


class WorkspaceService(
    BaseService,
):
    """
    Workspace business service.
    """

    # -------------------------------------------------------------------------
    # Construction
    # -------------------------------------------------------------------------

    def __init__(
        self,
        database: Session,
    ) -> None:
        """
        Initialize the workspace service.
        """

        super().__init__(
            database,
        )

        self._repository = WorkspaceRepository(
            database,
        )

        self._document_service = DocumentService(
            database,
        )

        self._storage = StorageService()

    # =========================================================================
    # Helpers
    # =========================================================================

    def _get_workspace(
        self,
        workspace_id: UUID,
    ) -> Workspace:
        """
        Retrieve a workspace or raise if it does not exist.
        """

        workspace = self._repository.get_by_id(
            workspace_id,
        )

        if workspace is None:
            raise ResourceNotFoundException(
                resource="Workspace",
                resource_id=str(workspace_id),
            )

        return workspace

    def _to_summary(
        self,
        workspace: Workspace,
    ) -> WorkspaceSummary:
        """
        Convert a Workspace model
        into a WorkspaceSummary.
        """

        return WorkspaceSummary(
            id=workspace.id,
            name=workspace.name,
            description=workspace.description,
            documents=0,
            knowledge=0,
            conversations=0,
            agents=0,
        )

    # =========================================================================
    # Queries
    # =========================================================================

    def get_workspaces(
        self,
    ) -> list[WorkspaceSummary]:
        """
        Retrieve all workspaces.
        """

        return [
            self._to_summary(
                workspace,
            )
            for workspace in self._repository.get_all()
        ]

    def get_workspace(
        self,
        workspace_id: UUID,
    ) -> WorkspaceSummary:
        """
        Retrieve a workspace.
        """

        workspace = self._get_workspace(
            workspace_id,
        )

        return self._to_summary(
            workspace,
        )

    # =========================================================================
    # Commands
    # =========================================================================

    def create_workspace(
        self,
        request: CreateWorkspaceRequest,
    ) -> WorkspaceSummary:
        """
        Create a workspace.
        """

        existing = self._repository.get_by_name(
            request.name,
        )

        if existing is not None:
            raise ResourceAlreadyExistsException(
                resource="Workspace",
                identifier=request.name,
            )

        workspace = Workspace(
            name=request.name,
            description=request.description,
            workspace_type=request.workspace_type,
            created_by="system",
        )

        with self.transaction():

            self._repository.save(
                workspace,
            )

        self.refresh(
            workspace,
        )

        return self._to_summary(
            workspace,
        )

    def update_workspace(
        self,
        workspace_id: UUID,
        request: UpdateWorkspaceRequest,
    ) -> WorkspaceSummary:
        """
        Update a workspace.
        """

        workspace = self._get_workspace(
            workspace_id,
        )

        if request.name is not None:
            workspace.name = request.name

        if request.description is not None:
            workspace.description = request.description

        with self.transaction():

            self._repository.save(
                workspace,
            )

        self.refresh(
            workspace,
        )

        return self._to_summary(
            workspace,
        )

    def delete_workspace(
        self,
        workspace_id: UUID,
    ) -> None:
        """
        Permanently delete a workspace.
        """

        workspace = self._get_workspace(
            workspace_id,
        )

        self._document_service.delete_workspace_documents(
            workspace_id,
        )

        self._storage.delete_workspace(
            workspace_id,
        )

        with self.transaction():

            self._repository.delete(
                workspace,
            )

    # =========================================================================
    # Bootstrap
    # =========================================================================

    def create_personal_workspace(
        self,
    ) -> Workspace:
        """
        Create the default personal workspace
        if one does not already exist.
        """

        workspace = self._repository.get_personal()

        if workspace is not None:
            return workspace

        workspace = Workspace(
            name="Personal Workspace",
            description="Your personal AI knowledge workspace.",
            workspace_type=WorkspaceType.PERSONAL,
            owner_id="system",
        )

        with self.transaction():

            self._repository.save(
                workspace,
            )

        self.refresh(
            workspace,
        )

        return workspace
