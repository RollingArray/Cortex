"""
Workspace Schemas

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines request and response schemas for
Workspace resources.

Features:
---------
- Workspace summary
- Workspace list
- Create workspace
- Update workspace
"""

# =============================================================================
# Imports
# =============================================================================

from backend.models.enums.workspace import WorkspaceType
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from uuid import UUID

# =============================================================================
# Workspace Summary
# =============================================================================


class WorkspaceSummary(BaseModel):
    """
    Workspace summary used throughout the UI.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    name: str

    description: str

    documents: int

    knowledge: int

    conversations: int

    agents: int


# =============================================================================
# Workspace List
# =============================================================================


class WorkspaceList(BaseModel):
    """
    Collection of workspaces.
    """

    workspaces: list[WorkspaceSummary]


# =============================================================================
# Create Workspace
# =============================================================================


class CreateWorkspaceRequest(BaseModel):
    """
    Create a new workspace.
    """

    name: str = Field(
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=500,
    )

    workspace_type: WorkspaceType = WorkspaceType.PERSONAL


# =============================================================================
# Update Workspace
# =============================================================================


class UpdateWorkspaceRequest(BaseModel):
    """
    Update an existing workspace.
    """

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=500,
    )
