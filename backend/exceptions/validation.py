"""
Base Exception

Author:
-------
Ranjoy Sen

Purpose:
--------
Validation Exception
"""

from backend.exceptions.base import CortexException


class BusinessRuleViolationException(
    CortexException,
):
    """
    Raised when a business rule
    has been violated.
    """

    def __init__(
        self,
        message: str,
    ) -> None:

        super().__init__(
            code="BUSINESS_RULE_VIOLATION",
            message=message,
        )
