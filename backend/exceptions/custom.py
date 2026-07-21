"""
Custom Exceptions

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the base exception used throughout
the Cortex platform.
"""

from backend.models.enums.error_code import ErrorCode


class CortexException(
    Exception,
):
    """
    Base Cortex exception.
    """

    def __init__(
        self,
        message: str,
        code: str = ErrorCode.CORTEX_ERROR,
        status_code: int = 400,
    ) -> None:

        super().__init__(
            message,
        )

        self.message = message
        self.code = code
        self.status_code = status_code
