"""
Service Dependencies

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides dependency injection helpers for
application services.

Features:
---------
- WorkspaceService dependency
- DocumentService dependency
"""

# =============================================================================
# Imports
# =============================================================================

from fastapi import Depends

from sqlalchemy.orm import Session

from backend.core.database import (
    get_database,
)

from backend.services.document.service import (
    DocumentService,
)

from backend.services.workspace.service import (
    WorkspaceService,
)

# =============================================================================
# Dependencies
# =============================================================================


def get_document_service(
    database: Session = Depends(
        get_database,
    ),
) -> DocumentService:
    """
    Returns a DocumentService instance.
    """

    return DocumentService(
        database,
    )


def get_workspace_service(
    database: Session = Depends(
        get_database,
    ),
) -> WorkspaceService:
    """
    Returns a WorkspaceService instance.
    """

    return WorkspaceService(
        database,
    )
