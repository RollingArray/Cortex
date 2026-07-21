"""
Already Exists Exception

Author:
-------
Ranjoy Sen

Purpose:
--------
Raised when attempting to create
a resource that already exists.
"""

from fastapi import status

from backend.exceptions.base import CortexException
from backend.models.enums.error_code import ErrorCode


class ResourceAlreadyExistsException(
    CortexException,
):
    """
    Raised when attempting to create
    a duplicate resource.
    """

    def __init__(
        self,
        resource: str,
        identifier: str | None = None,
    ) -> None:

        if identifier:
            message = f"{resource} '{identifier}' already exists."
        else:
            message = f"{resource} already exists."

        super().__init__(
            message=message,
            code=ErrorCode.RESOURCE_ALREADY_EXISTS,
            status_code=409,
        )
