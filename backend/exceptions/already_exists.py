"""
Base Exception

Author:
-------
Ranjoy Sen

Purpose:
--------
Already Exists Exception
"""

from backend.exceptions.base import CortexError


class ResourceAlreadyExistsError(
    CortexError,
):
    """
    Raised when attempting to create
    a duplicate resource.
    """

    def __init__(
        self,
        resource: str,
    ) -> None:

        super().__init__(
            f"{resource} already exists.",
        )

        self.resource = resource
