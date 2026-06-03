from app.services.ai.base import AIProvider


class MockProvider(AIProvider):

    async def generate(
        self,
        prompt: str,
    ) -> str:

        return (
            f"Mock response for: {prompt}"
        )