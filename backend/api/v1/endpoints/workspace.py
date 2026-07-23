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

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    File,
    Response,
    UploadFile,
    status,
)

from sqlalchemy.orm import (
    Session,
)

from backend.core.database import (
    get_database,
)

from backend.di.services import get_document_service, get_workspace_service
from backend.schemas.document import DocumentResponse, DocumentUploadResponse
from backend.schemas.workspace import (
    WorkspaceSummary,
    CreateWorkspaceRequest,
    UpdateWorkspaceRequest,
)

from backend.services.document.service import DocumentService
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
    service: WorkspaceService = Depends(
        get_workspace_service,
    ),
) -> list[WorkspaceSummary]:
    """
    Retrieve all available workspaces.
    """

    return service.get_workspaces()


@router.get(
    "/{workspace_id}",
    response_model=WorkspaceSummary,
)
async def get_workspace(
    workspace_id: UUID,
    service: WorkspaceService = Depends(
        get_workspace_service,
    ),
) -> WorkspaceSummary:
    """
    Retrieve a workspace by identifier.
    """

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
    service: WorkspaceService = Depends(
        get_workspace_service,
    ),
) -> WorkspaceSummary:
    """
    Create a new workspace.
    """

    return service.create_workspace(
        request,
    )


@router.patch(
    "/{workspace_id}",
    response_model=WorkspaceSummary,
)
async def update_workspace(
    workspace_id: UUID,
    request: UpdateWorkspaceRequest,
    service: WorkspaceService = Depends(
        get_workspace_service,
    ),
) -> WorkspaceSummary:
    """
    Update an existing workspace.
    """

    return service.update_workspace(
        workspace_id=workspace_id,
        request=request,
    )


@router.delete(
    "/{workspace_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_workspace(
    workspace_id: UUID,
    service: WorkspaceService = Depends(
        get_workspace_service,
    ),
) -> Response:
    """
    Delete a workspace.
    """

    service.delete_workspace(
        workspace_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.post(
    "/{workspace_id}/documents",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    workspace_id: UUID,
    file: UploadFile = File(...),
    service: DocumentService = Depends(
        get_document_service,
    ),
) -> DocumentUploadResponse:
    """
    Upload a document into a workspace.
    """

    document = service.upload_document(
        workspace_id=workspace_id,
        file=file,
    )

    return DocumentUploadResponse(
        document=DocumentResponse.model_validate(
            document,
        ),
    )
