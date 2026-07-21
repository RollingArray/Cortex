"""
Document Exceptions
"""

from backend.exceptions.base import CortexException
from backend.models.enums.error_code import ErrorCode


class UnsupportedDocumentTypeException(CortexException):
    """
    Raised when attempting to upload
    an unsupported document type.
    """

    def __init__(
        self,
        extension: str,
    ) -> None:

        super().__init__(
            message=f"Document type '{extension}' is not supported.",
            code=ErrorCode.UNSUPPORTED_DOCUMENT_TYPE,
            status_code=415,
        )
