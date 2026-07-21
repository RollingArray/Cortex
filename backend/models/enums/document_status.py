"""
Document Status

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the lifecycle states of a document within the Cortex
knowledge management platform.

Allowed State Transitions

UPLOADED
    -> QUEUED

QUEUED
    -> PROCESSING

PROCESSING
    -> PROCESSED
    -> FAILED

FAILED
    -> QUEUED
"""

from enum import Enum


class DocumentStatus(str, Enum):
    """
    Represents the processing lifecycle of a document.
    """

    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    READY = "READY"
    FAILED = "FAILED"
    DELETED = "DELETED"
    ARCHIVED = "ARCHIVED"
