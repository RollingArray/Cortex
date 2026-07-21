"""
Document Model

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the Document database entity.

Features:
---------
- Workspace association
- File storage metadata
- Processing status
- Enterprise document intelligence foundation

Lifecycle
---------
UPLOADED
    ↓
QUEUED
    ↓
PROCESSING
 ┌──────────────┴──────────────┐
 ▼                             ▼
PROCESSED                  FAILED
    ↓
SOFT DELETED

Allowed State Transitions
-------------------------
UPLOADED    -> QUEUED
QUEUED      -> PROCESSING
PROCESSING  -> PROCESSED
PROCESSING  -> FAILED
FAILED      -> QUEUED
"""

# =============================================================================
# Imports
# =============================================================================

from typing import TYPE_CHECKING

from uuid import UUID

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Enum,
    ForeignKey,
    Index,
    JSON,
    String,
)
from sqlalchemy.ext.mutable import MutableDict

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.models.entity import Entity
from backend.models.enums import DocumentStatus
from backend.models.constants import (
    CHECKSUM_LENGTH,
    CONTENT_TYPE_LENGTH,
    ERROR_MESSAGE_LENGTH,
    FILENAME_LENGTH,
    PATH_LENGTH,
)
from backend.models.traits import (
    SoftDeletable,
    Auditable,
)

if TYPE_CHECKING:
    from backend.models.domain.workspace import Workspace

# =============================================================================
# Document
# =============================================================================


class Document(
    Auditable,
    SoftDeletable,
    Entity,
):
    """
    Document database entity.

    Traits
    ------
    - Auditable
    - SoftDeletable
    """

    __tablename__ = "documents"

    __table_args__ = (
        CheckConstraint(
            "size_bytes >= 0",
            name="document_size_non_negative",
        ),
        CheckConstraint(
            "(page_count IS NULL) OR (page_count >= 0)",
            name="document_page_count_non_negative",
        ),
        CheckConstraint(
            "processing_progress >= 0 " "AND processing_progress <= 100",
            name="document_processing_progress_valid",
        ),
        Index(
            "ix_documents_workspace_id",
            "workspace_id",
        ),
        Index(
            "ix_documents_status",
            "status",
        ),
        Index(
            "ix_documents_checksum",
            "checksum",
        ),
        Index(
            "ix_documents_deleted_at",
            "deleted_at",
        ),
    )

    # -------------------------------------------------------------------------
    # Foreign Keys
    # -------------------------------------------------------------------------

    workspace_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "workspaces.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Storage
    # -------------------------------------------------------------------------

    original_filename: Mapped[str] = mapped_column(
        String(FILENAME_LENGTH),
        nullable=False,
    )

    storage_filename: Mapped[str] = mapped_column(
        String(FILENAME_LENGTH),
        nullable=False,
    )

    storage_path: Mapped[str] = mapped_column(
        String(PATH_LENGTH),
        nullable=False,
    )

    content_type: Mapped[str] = mapped_column(
        String(CONTENT_TYPE_LENGTH),
        nullable=False,
    )

    size_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    checksum: Mapped[str] = mapped_column(
        String(CHECKSUM_LENGTH),
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # File Metadata
    # -------------------------------------------------------------------------

    page_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    # -------------------------------------------------------------------------
    # Document Metadata
    # -------------------------------------------------------------------------

    document_metadata: Mapped[dict | None] = mapped_column(
        MutableDict.as_mutable(JSON),
        nullable=True,
    )

    # -------------------------------------------------------------------------
    # Processing
    # -------------------------------------------------------------------------

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(
            DocumentStatus,
            native_enum=False,
            create_constraint=True,
            validate_strings=True,
        ),
        default=DocumentStatus.UPLOADED,
        nullable=False,
    )

    processing_progress: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    processing_error: Mapped[str | None] = mapped_column(
        String(ERROR_MESSAGE_LENGTH),
        nullable=True,
    )

    processing_details: Mapped[dict | None] = mapped_column(
        MutableDict.as_mutable(JSON),
        nullable=True,
    )

    # -------------------------------------------------------------------------
    # Relationships
    # -------------------------------------------------------------------------

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        back_populates="documents",
        lazy="selectin",
    )

    # -------------------------------------------------------------------------
    # Chunks
    # -------------------------------------------------------------------------

    chunk_count: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Representation
    # -------------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Document("
            f"id={self.id!r}, "
            f"file={self.original_filename!r}, "
            f"status={self.status.value!r}, "
            f"progress={self.processing_progress}%"
            f")"
        )
