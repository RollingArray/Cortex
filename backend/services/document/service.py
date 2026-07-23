"""
Document Service

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides business logic for
Document management.

Features:
---------
- Upload document
- Retrieve document
- List workspace documents
- Delete document
"""

from __future__ import annotations

from uuid import UUID, uuid4

from pathlib import Path

from fastapi import UploadFile

from sqlalchemy.orm import Session

from backend.exceptions.already_exists import (
    ResourceAlreadyExistsException,
)
from backend.exceptions.document_type import UnsupportedDocumentTypeException
from backend.exceptions.resource import (
    ResourceNotFoundException,
)

from backend.models.domain.document import Document
from backend.models.enums import DocumentStatus

from backend.repositories.document.repository import (
    DocumentRepository,
)
from backend.repositories.workspace.repository import (
    WorkspaceRepository,
)

from backend.services.storage.service import StorageService

from backend.services.base import (
    BaseService,
)

SUPPORTED_DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".csv",
    ".ppt",
    ".pptx",
    ".txt",
    ".md",
}


class DocumentService(
    BaseService,
):
    """
    Service responsible for Document business operations.
    """

    def __init__(
        self,
        database: Session,
    ) -> None:
        """
        Initialize the document service.
        """

        super().__init__(
            database,
        )

        self._repository = DocumentRepository(
            database,
        )

        self._workspace_repository = WorkspaceRepository(
            database,
        )

        self._storage = StorageService()

    # =========================================================================
    # Helpers
    # =========================================================================
    def _delete_document(
        self,
        document: Document,
    ) -> None:
        """
        Delete all resources associated with a document.

        This method assumes the caller is responsible
        for transaction management.
        """

        #
        # Delete physical document.
        #

        self._storage.delete_document(
            document.storage_directory,
            document.storage_filename,
        )

        #
        # TODO
        #
        # Delete parsed document
        # Delete chunks
        # Delete embeddings
        # Delete vector index
        # Delete extracted metadata
        #

        self._repository.delete(
            document,
        )

    # =========================================================================
    # Commands
    # =========================================================================

    def upload_document(
        self,
        workspace_id: UUID,
        file: UploadFile,
    ) -> Document:
        """
        Upload a document to a workspace.
        """

        # ---------------------------------------------------------------------
        # Validate workspace
        # ---------------------------------------------------------------------

        workspace = self._workspace_repository.get_by_id(
            workspace_id,
        )

        if workspace is None:
            raise ResourceNotFoundException(
                resource="Workspace",
                resource_id=str(workspace_id),
            )

        # ---------------------------------------------------------------------
        # Validate filename
        # ---------------------------------------------------------------------

        filename = file.filename

        if not filename:
            raise ValueError(
                "Uploaded file must have a filename.",
            )

        extension = Path(
            filename,
        ).suffix.lower()

        if extension not in SUPPORTED_DOCUMENT_EXTENSIONS:
            raise UnsupportedDocumentTypeException(
                extension=extension,
            )

        # ---------------------------------------------------------------------
        # Generate storage location
        # ---------------------------------------------------------------------

        document_id = uuid4()

        storage_directory = self._storage.build_workspace_directory(
            workspace_id,
        )

        storage_filename = self._storage.build_storage_filename(
            document_id,
            filename,
        )

        try:

            # -------------------------------------------------------------
            # Save file
            # -------------------------------------------------------------

            size_bytes, checksum = self._storage.save_document(
                file=file,
                storage_directory=storage_directory,
                storage_filename=storage_filename,
            )

            # -------------------------------------------------------------
            # Duplicate detection
            # -------------------------------------------------------------

            if self._repository.exists_duplicate(
                workspace_id=workspace_id,
                checksum=checksum,
            ):
                raise ResourceAlreadyExistsException(
                    resource="Document",
                    identifier=filename,
                )

            # -------------------------------------------------------------
            # Create document
            # -------------------------------------------------------------

            document = Document(
                id=document_id,
                workspace_id=workspace_id,
                original_filename=filename,
                storage_directory=str(
                    storage_directory,
                ),
                storage_filename=storage_filename,
                content_type=file.content_type or "application/octet-stream",
                size_bytes=size_bytes,
                checksum=checksum,
                status=DocumentStatus.UPLOADED,
                processing_progress=0,
            )

            with self.transaction():

                self._repository.create(
                    document,
                )

            self.refresh(
                document,
            )

            return document

        except Exception:

            self._storage.delete_document(
                storage_directory,
                storage_filename,
            )

            raise

        finally:

            file.file.close()

    # =========================================================================
    # Queries
    # =========================================================================

    def get_document(
        self,
        document_id: UUID,
    ) -> Document | None:
        """
        Retrieve a document.
        """

        return self._repository.get_by_id(
            document_id,
        )

    def list_documents(
        self,
        workspace_id: UUID,
    ) -> list[Document]:
        """
        Retrieve workspace documents.
        """

        return self._repository.list_by_workspace(
            workspace_id,
        )

    # =========================================================================
    # Delete
    # =========================================================================

    def delete_document(
        self,
        document_id: UUID,
    ) -> bool:
        """
        Permanently delete a document.
        """

        document = self._repository.get_by_id(
            document_id,
        )

        if document is None:
            return False

        with self.transaction():

            self._delete_document(
                document,
            )

        return True

    def delete_workspace_documents(
        self,
        workspace_id: UUID,
    ) -> None:
        """
        Permanently delete all documents
        belonging to a workspace.
        """

        documents = self._repository.list_by_workspace(
            workspace_id,
        )

        with self.transaction():

            for document in documents:

                self._delete_document(
                    document,
                )
