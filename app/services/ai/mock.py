from app.services.ai.base import AIProvider


class MockProvider(AIProvider):
    """
    Mock AI provider used for local development
    and automated testing.
    """

    async def generate(
        self,
        prompt: str,
    ) -> str:
        return (
            f"Mock response for: {prompt}"
        )