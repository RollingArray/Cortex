"""
Checksum Utilities

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides checksum calculation utilities
for files.

Features:
---------
- SHA-256 checksum generation
"""

from __future__ import annotations

import hashlib
from pathlib import Path


def calculate_sha256(
    file_path: Path,
) -> str:
    """
    Calculate the SHA-256 checksum of a file.

    Parameters
    ----------
    file_path : Path
        Path to the file.

    Returns
    -------
    str
        Hexadecimal SHA-256 checksum.
    """

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:

        while chunk := file.read(8192):

            sha256.update(
                chunk,
            )

    return sha256.hexdigest()
