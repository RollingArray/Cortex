class CortexException(Exception):

    def __init__(
        self,
        message: str,
        code: str = "CORTEX_ERROR"
    ):
        self.message = message
        self.code = code

        super().__init__(message)