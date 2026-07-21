"""
Base Exception

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the base exception used throughout
the Cortex platform.
"""


class CortexError(
    Exception,
):
    """
    Base exception for all Cortex
    domain errors.
    """

    def __init__(
        self,
        message: str,
    ) -> None:

        super().__init__(
            message,
        )

        self.message = message
