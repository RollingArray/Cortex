"""
Workspace Model

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the Workspace database entity.

Features:
---------
- Workspace identity
- Workspace classification
- Document relationship

Deletion Policy
---------------
- Workspaces are permanently deleted.
- Deleting a workspace cascades to all associated documents.

"""

# =============================================================================
# Imports
# =============================================================================

from typing import TYPE_CHECKING

from sqlalchemy import (
    CheckConstraint,
    Enum,
    Index,
    String,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.models.entity import Entity
from backend.models.enums.workspace import WorkspaceType
from backend.models.constants import (
    DEFAULT_DESCRIPTION,
    DESCRIPTION_LENGTH,
    NAME_LENGTH,
)
from backend.models.traits import (
    Auditable,
    Ownable,
)

if TYPE_CHECKING:
    from backend.models.domain.document import Document

# =============================================================================
# Workspace
# =============================================================================


class Workspace(
    Auditable,
    Ownable,
    Entity,
):
    """
    Workspace database entity.

    Traits
    ------
    - Auditable
    - Ownable
    """

    __tablename__ = "workspaces"

    __table_args__ = (
        UniqueConstraint(
            "name",
            name="workspace_name_unique",
        ),
        CheckConstraint(
            "length(name) > 0",
            name="workspace_name_not_empty",
        ),
        Index(
            "ix_workspaces_workspace_type",
            "workspace_type",
        ),
    )

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    name: Mapped[str] = mapped_column(
        String(NAME_LENGTH),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(DESCRIPTION_LENGTH),
        default=DEFAULT_DESCRIPTION,
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Classification
    # -------------------------------------------------------------------------

    workspace_type: Mapped[WorkspaceType] = mapped_column(
        Enum(
            WorkspaceType,
            native_enum=False,
            create_constraint=True,
            validate_strings=True,
        ),
        default=WorkspaceType.PERSONAL,
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Relationships
    # -------------------------------------------------------------------------

    documents: Mapped[list["Document"]] = relationship(
        "Document",
        back_populates="workspace",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    # -------------------------------------------------------------------------
    # Representation
    # -------------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Workspace("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"type={self.workspace_type.value!r}"
            f")"
        )
