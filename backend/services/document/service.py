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

import shutil
from pathlib import Path
from uuid import UUID, uuid4

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

from backend.utils.checksum import calculate_sha256

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


class DocumentService:
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

        self._repository = DocumentRepository(
            database,
        )

        self._workspace_repository = WorkspaceRepository(
            database,
        )

    # =========================================================================
    # Helpers
    # =========================================================================

    def _build_storage_path(
        self,
        workspace_id: UUID,
        filename: str,
        document_id: UUID,
    ) -> Path:
        """
        Build the storage path for a document.
        """

        extension = Path(filename).suffix

        workspace_directory = Path("storage") / "workspaces" / str(workspace_id)

        workspace_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return workspace_directory / f"{document_id}{extension}"

    def _save_file(
        self,
        file: UploadFile,
        destination: Path,
    ) -> tuple[int, str]:
        """
        Save uploaded file to storage.

        Returns
        -------
        tuple[int, str]
            (size_bytes, checksum)
        """

        with destination.open("wb") as output:
            shutil.copyfileobj(
                file.file,
                output,
            )

        size_bytes = destination.stat().st_size

        checksum = calculate_sha256(
            destination,
        )

        return (
            size_bytes,
            checksum,
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
            raise ValueError("Uploaded file must have a filename.")

        extension = Path(filename).suffix.lower()

        if extension not in SUPPORTED_DOCUMENT_EXTENSIONS:
            raise UnsupportedDocumentTypeException(
                extension=extension,
            )

        # ---------------------------------------------------------------------
        # Generate document identifier
        # ---------------------------------------------------------------------

        document_id = uuid4()

        destination = self._build_storage_path(
            workspace_id=workspace_id,
            filename=filename,
            document_id=document_id,
        )

        try:

            # -------------------------------------------------------------
            # Save file
            # -------------------------------------------------------------

            size_bytes, checksum = self._save_file(
                file=file,
                destination=destination,
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
                storage_filename=destination.name,
                storage_path=str(destination),
                content_type=(file.content_type or "application/octet-stream"),
                size_bytes=size_bytes,
                checksum=checksum,
                status=DocumentStatus.UPLOADED,
                processing_progress=0,
            )

            return self._repository.create(
                document,
            )

        except Exception:

            if destination.exists():
                destination.unlink()

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
        Soft delete a document.
        """

        document = self._repository.get_by_id(
            document_id,
        )

        if document is None:
            return False

        self._repository.delete(
            document,
        )

        return True
