"""
Base Service

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides common transaction management
for all application services.

Features:
---------
- Refresh entities
- Transaction context manager
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from sqlalchemy.orm import Session


class BaseService:
    """
    Base class for application services.
    """

    def __init__(
        self,
        database: Session,
    ) -> None:
        self._database = database

    def refresh(
        self,
        entity: Any,
    ) -> None:
        """
        Refresh an entity from the database.
        """

        self._database.refresh(
            entity,
        )

    @contextmanager
    def transaction(
        self,
    ) -> Iterator[None]:
        """
        Execute a database transaction.

        Commits on success and rolls back
        on failure.
        """

        try:

            yield

            self._database.commit()

        except Exception:

            self._database.rollback()

            raise
