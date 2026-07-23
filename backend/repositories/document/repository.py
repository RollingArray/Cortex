"""
Document Repository

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides data access operations for
Document entities.

Features:
---------
- Persist document
- Retrieve document
- Retrieve document by checksum
- List workspace documents
- Permanently delete document
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.domain.document import Document

# =============================================================================
# Repository
# =============================================================================


class DocumentRepository:
    """
    Repository responsible for Document persistence.
    """

    # -------------------------------------------------------------------------
    # Construction
    # -------------------------------------------------------------------------

    def __init__(
        self,
        database: Session,
    ) -> None:
        """
        Initialize repository.

        Parameters
        ----------
        database : Session
            Active SQLAlchemy database session.
        """

        self._database = database

    # -------------------------------------------------------------------------
    # Queries
    # -------------------------------------------------------------------------

    def get_by_id(
        self,
        document_id: UUID,
    ) -> Document | None:
        """
        Retrieve a document by identifier.
        """

        statement = select(
            Document,
        ).where(
            Document.id == document_id,
        )

        return self._database.scalar(
            statement,
        )

    def get_by_workspace_and_checksum(
        self,
        workspace_id: UUID,
        checksum: str,
    ) -> Document | None:
        """
        Retrieve a document by checksum
        within a workspace.
        """

        statement = select(
            Document,
        ).where(
            Document.workspace_id == workspace_id,
            Document.checksum == checksum,
        )

        return self._database.scalar(
            statement,
        )

    def list_by_workspace(
        self,
        workspace_id: UUID,
    ) -> list[Document]:
        """
        Retrieve all documents
        belonging to a workspace.
        """

        statement = (
            select(
                Document,
            )
            .where(
                Document.workspace_id == workspace_id,
            )
            .order_by(
                Document.created_at.desc(),
            )
        )

        return list(
            self._database.scalars(
                statement,
            ).all()
        )

    # -------------------------------------------------------------------------
    # Commands
    # -------------------------------------------------------------------------

    def create(
        self,
        document: Document,
    ) -> Document:

        self._database.add(
            document,
        )

        return document

    def save(
        self,
        document: Document,
    ) -> Document:

        self._database.add(
            document,
        )

        return document

    def delete(
        self,
        document: Document,
    ) -> None:

        self._database.delete(
            document,
        )

    def exists_duplicate(
        self,
        workspace_id: UUID,
        checksum: str,
    ) -> bool:
        """
        Check whether a document with the same checksum
        already exists within the workspace.
        """

        statement = (
            select(
                Document.id,
            )
            .where(
                Document.workspace_id == workspace_id,
                Document.checksum == checksum,
            )
            .limit(
                1,
            )
        )

        return (
            self._database.scalar(
                statement,
            )
            is not None
        )
