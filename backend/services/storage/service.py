"""
Storage Service

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides all filesystem operations for Cortex.

Features:
---------
- Workspace directory management
- Document storage
- Document deletion
- Workspace deletion
- Filesystem path resolution
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import shutil

from pathlib import Path
from uuid import UUID

from fastapi import UploadFile

from backend.core.config import settings
from backend.utils.checksum import calculate_sha256

# =============================================================================
# Service
# =============================================================================


class StorageService:
    """
    Filesystem abstraction for Cortex.

    Architectural Rules
    -------------------
    - Only StorageService knows where files are physically stored.
    - Services exchange logical storage information only.
    - No service constructs filesystem paths.
    """

    # =========================================================================
    # Construction
    # =========================================================================

    def __init__(
        self,
    ) -> None:

        self._storage_root = Path(
            settings.storage_path,
        )

    # =========================================================================
    # Logical Storage Helpers
    # =========================================================================

    def build_workspace_directory(
        self,
        workspace_id: UUID,
    ) -> Path:
        """
        Return the logical workspace directory.

        Example
        -------
        workspaces/<workspace_id>
        """

        return Path("workspaces") / str(workspace_id)

    def build_storage_filename(
        self,
        document_id: UUID,
        original_filename: str,
    ) -> str:
        """
        Return the storage filename.

        Example
        -------
        6ab7e8d9.pdf
        """

        extension = Path(
            original_filename,
        ).suffix.lower()

        return f"{document_id}{extension}"

    # =========================================================================
    # Filesystem Resolution
    # =========================================================================

    def absolute_directory(
        self,
        storage_directory: str | Path,
    ) -> Path:
        """
        Resolve a logical storage directory into an
        absolute filesystem directory.
        """

        return self._storage_root / Path(storage_directory)

    def absolute_path(
        self,
        storage_directory: str | Path,
        storage_filename: str,
    ) -> Path:
        """
        Resolve a logical storage location into an
        absolute filesystem path.
        """

        return (
            self.absolute_directory(
                storage_directory,
            )
            / storage_filename
        )

    # =========================================================================
    # Internal Helpers
    # =========================================================================

    def _remove_empty_directory(
        self,
        directory: Path,
    ) -> None:
        """
        Remove a directory if it exists and is empty.
        """

        if directory.exists() and directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()

    # =========================================================================
    # Document Operations
    # =========================================================================

    def save_document(
        self,
        file: UploadFile,
        storage_directory: str | Path,
        storage_filename: str,
    ) -> tuple[int, str]:
        """
        Save an uploaded document.

        Returns
        -------
        tuple[int, str]

            (
                size_bytes,
                checksum,
            )
        """

        destination = self.absolute_path(
            storage_directory,
            storage_filename,
        )

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "wb",
        ) as output:

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

    def delete_document(
        self,
        storage_directory: str | Path,
        storage_filename: str,
    ) -> None:
        """
        Delete a document.

        If the workspace directory becomes empty,
        it is automatically removed.
        """

        path = self.absolute_path(
            storage_directory,
            storage_filename,
        )

        if not path.exists():
            return

        workspace_directory = path.parent

        path.unlink()

        self._remove_empty_directory(
            workspace_directory,
        )

    # =========================================================================
    # Workspace Operations
    # =========================================================================

    def delete_workspace(
        self,
        workspace_id: UUID,
    ) -> None:
        """
        Delete an entire workspace directory.
        """

        directory = self.absolute_directory(
            self.build_workspace_directory(
                workspace_id,
            )
        )

        if directory.exists():

            shutil.rmtree(
                directory,
            )

    # =========================================================================
    # Utility
    # =========================================================================

    def exists(
        self,
        storage_directory: str | Path,
        storage_filename: str,
    ) -> bool:
        """
        Determine whether a document exists.
        """

        return self.absolute_path(
            storage_directory,
            storage_filename,
        ).exists()
