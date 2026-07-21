"""
Document Endpoints

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides REST API endpoints for managing
Document resources.

Features:
---------
- Retrieve workspace documents
- Retrieve document
- Upload document
- Delete document
"""

# =============================================================================
# Imports
# =============================================================================

from uuid import UUID

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

from backend.repositories.document.repository import DocumentRepository
from backend.schemas.document import (
    DocumentDeleteResponse,
    DocumentListResponse,
    DocumentResponse,
)

from backend.services.document.service import (
    DocumentService,
)

# =============================================================================
# Router
# =============================================================================

router = APIRouter(
    prefix="/documents",
    tags=[
        "Document",
    ],
)

# =============================================================================
# Endpoints
# =============================================================================


@router.get(
    "/workspaces/{workspace_id}",
    response_model=DocumentListResponse,
)
async def get_documents(
    workspace_id: UUID,
    database: Session = Depends(
        get_database,
    ),
) -> DocumentListResponse:
    """
    Retrieve all documents belonging to a workspace.
    """

    service = DocumentService(
        database,
    )

    documents = service.list_documents(
        workspace_id,
    )

    return DocumentListResponse(
        documents=[DocumentResponse.model_validate(document) for document in documents],
    )


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
async def get_document(
    document_id: UUID,
    database: Session = Depends(
        get_database,
    ),
) -> DocumentResponse:
    """
    Retrieve a document by identifier.
    """

    repository = DocumentRepository(
        database,
    )

    service = DocumentService(
        database,
    )

    document = service.get_document(
        document_id,
    )

    return DocumentResponse.model_validate(
        document,
    )


@router.delete(
    "/{document_id}",
    response_model=DocumentDeleteResponse,
)
async def delete_document(
    document_id: UUID,
    database: Session = Depends(
        get_database,
    ),
) -> DocumentDeleteResponse:
    """
    Delete a document.
    """

    repository = DocumentRepository(
        database,
    )

    service = DocumentService(
        repository,
    )

    service.delete_document(
        document_id,
    )

    return DocumentDeleteResponse()
