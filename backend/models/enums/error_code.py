"""
Error Codes

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines standard error codes used
throughout the Cortex platform.
"""

# =============================================================================
# Imports
# =============================================================================

from enum import (
    StrEnum,
)

# =============================================================================
# Error Codes
# =============================================================================


class ErrorCode(StrEnum):
    """
    Standard Cortex error codes.
    """

    # -------------------------------------------------------------------------
    # Generic
    # -------------------------------------------------------------------------

    CORTEX_ERROR = "CORTEX_ERROR"

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    BUSINESS_RULE_VIOLATION = "BUSINESS_RULE_VIOLATION"

    # -------------------------------------------------------------------------
    # Resources
    # -------------------------------------------------------------------------

    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"

    RESOURCE_ALREADY_EXISTS = "RESOURCE_ALREADY_EXISTS"

    # -------------------------------------------------------------------------
    # Authentication
    # -------------------------------------------------------------------------

    UNAUTHORIZED = "UNAUTHORIZED"

    FORBIDDEN = "FORBIDDEN"

    # -------------------------------------------------------------------------
    # Validation
    # -------------------------------------------------------------------------

    INVALID_REQUEST = "INVALID_REQUEST"
