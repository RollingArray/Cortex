"""
Database Model Constants

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines common constants shared across all Cortex
database models.

Features:
---------
- Database string lengths
- Common numeric limits
- Shared model constants

Notes:
------
All database models should reference these constants
instead of using hard-coded values.
"""

# =============================================================================
# Identifier Lengths
# =============================================================================

UUID_LENGTH = 36

PRINCIPAL_ID_LENGTH = 255

# =============================================================================
# Business Data Lengths
# =============================================================================

NAME_LENGTH = 100

DESCRIPTION_LENGTH = 500

TITLE_LENGTH = 255

# =============================================================================
# File Storage Lengths
# =============================================================================

FILENAME_LENGTH = 255

PATH_LENGTH = 1000

CONTENT_TYPE_LENGTH = 100

CHECKSUM_LENGTH = 64

# =============================================================================
# Classification Lengths
# =============================================================================

ENUM_LENGTH = 20

# =============================================================================
# Processing Lengths
# =============================================================================

ERROR_MESSAGE_LENGTH = 1000

# =============================================================================
# Database Defaults
# =============================================================================

DEFAULT_DESCRIPTION = ""
