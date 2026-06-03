from app.core.config import (
    AIProvider,
    settings,
)

from app.services.ai.base import AIProvider as BaseAIProvider
from app.services.ai.mock import MockProvider


def get_ai_provider() -> BaseAIProvider:
    """
    Factory responsible for returning
    the configured AI provider.
    """

    match settings.ai_provider:

        case AIProvider.MOCK:
            return MockProvider()

        case AIProvider.OLLAMA:
            raise NotImplementedError(
                "Ollama provider is not yet enabled"
            )

        case _:
            raise ValueError(
                (
                    "Unsupported AI provider: "
                    f"{settings.ai_provider}"
                )
            )