"""
Workspace Endpoints

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides REST API endpoints for managing
Workspace resources.

Features:
---------
- Retrieve all workspaces
- Retrieve workspace
- Create workspace
- Update workspace
- Delete workspace
"""

# =============================================================================
# Imports
# =============================================================================

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from sqlalchemy.orm import (
    Session,
)

from backend.core.database import (
    get_database,
)

from backend.schemas.workspace import (
    WorkspaceSummary,
    CreateWorkspaceRequest,
    UpdateWorkspaceRequest,
)

from backend.services.workspace import (
    WorkspaceService,
)

# =============================================================================
# Router
# =============================================================================

router = APIRouter(
    prefix="/workspaces",
    tags=[
        "Workspace",
    ],
)

# =============================================================================
# Endpoints
# =============================================================================


@router.get(
    "",
    response_model=list[WorkspaceSummary],
)
async def get_workspaces(
    database: Session = Depends(
        get_database,
    ),
) -> list[WorkspaceSummary]:
    """
    Retrieve all available workspaces.
    """

    service = WorkspaceService(
        database,
    )

    return service.get_workspaces()


@router.get(
    "/{workspace_id}",
    response_model=WorkspaceSummary,
)
async def get_workspace(
    workspace_id: str,
    database: Session = Depends(
        get_database,
    ),
) -> WorkspaceSummary:
    """
    Retrieve a workspace by identifier.
    """

    service = WorkspaceService(
        database,
    )

    return service.get_workspace(
        workspace_id,
    )


@router.post(
    "",
    response_model=WorkspaceSummary,
    status_code=status.HTTP_201_CREATED,
)
async def create_workspace(
    request: CreateWorkspaceRequest,
    database: Session = Depends(
        get_database,
    ),
) -> WorkspaceSummary:
    """
    Create a new workspace.
    """

    service = WorkspaceService(
        database,
    )

    return service.create_workspace(
        request,
    )


@router.patch(
    "/{workspace_id}",
    response_model=WorkspaceSummary,
)
async def update_workspace(
    workspace_id: str,
    request: UpdateWorkspaceRequest,
    database: Session = Depends(
        get_database,
    ),
) -> WorkspaceSummary:
    """
    Update an existing workspace.
    """

    service = WorkspaceService(
        database,
    )

    return service.update_workspace(
        workspace_id=workspace_id,
        request=request,
    )


@router.delete(
    "/{workspace_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_workspace(
    workspace_id: str,
    database: Session = Depends(
        get_database,
    ),
) -> Response:
    """
    Delete a workspace.
    """

    service = WorkspaceService(
        database,
    )

    service.delete_workspace(
        workspace_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
