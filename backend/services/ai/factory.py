from functools import lru_cache

from backend.core.config import (
    AIProvider,
    settings,
)

from backend.services.ai.mock import (
    MockProvider,
)

from backend.services.ai.ollama import (
    OllamaProvider,
)


@lru_cache
def get_ai_provider():

    match settings.ai_provider:

        case AIProvider.MOCK:
            return MockProvider()

        case AIProvider.OLLAMA:
            return OllamaProvider()

        case _:
            raise ValueError(
                (
                    "Unsupported provider: "
                    f"{settings.ai_provider}"
                )
            )