"""
Base Exception

Author:
-------
Ranjoy Sen

Purpose:
--------
Resource Not Found Exception
"""

from backend.exceptions.base import CortexException


class ResourceNotFoundError(
    CortexException,
):
    """
    Raised when a requested resource
    cannot be found.
    """

    def __init__(
        self,
        resource: str,
        resource_id: str,
    ) -> None:

        super().__init__(
            f"{resource} '{resource_id}' was not found.",
        )

        self.resource = resource
        self.resource_id = resource_id
