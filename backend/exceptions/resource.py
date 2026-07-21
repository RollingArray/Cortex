"""
Resource Exceptions

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines resource-related exceptions.
"""

from backend.exceptions.base import CortexException
from backend.models.enums.error_code import ErrorCode


class ResourceNotFoundException(
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
            code=ErrorCode.RESOURCE_NOT_FOUND,
            message=f"{resource} '{resource_id}' was not found.",
        )


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
        value: str,
    ) -> None:

        super().__init__(
            code=ErrorCode.RESOURCE_ALREADY_EXISTS,
            message=f"{resource} '{value}' already exists.",
        )
