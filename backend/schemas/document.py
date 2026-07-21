"""
Document Schemas

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines API request and response
schemas for Document management.

Features:
---------
- Document response
- Upload response
- List response
- Delete response
"""

from datetime import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    computed_field,
)

from backend.models.enums.document_status import DocumentStatus


class DocumentResponse(BaseModel):
    """
    Represents a document returned by the API.
    """

    id: UUID
    workspace_id: UUID

    original_filename: str
    content_type: str
    size_bytes: int
    checksum: str

    status: DocumentStatus
    processing_progress: int

    page_count: int | None = None
    chunk_count: int = 0

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )

    @computed_field
    @property
    def download_url(self) -> str:
        """
        Download endpoint for the document.
        """

        return f"/api/v1/documents/{self.id}/download"


class DocumentUploadResponse(BaseModel):
    """
    Response returned after a successful document upload.
    """

    message: str = "Document uploaded successfully."
    document: DocumentResponse


class DocumentListResponse(BaseModel):
    """
    Response returned when listing documents.
    """

    documents: list[DocumentResponse]


class DocumentDeleteResponse(BaseModel):
    """
    Response returned after deleting a document.
    """

    message: str = "Document deleted successfully."
