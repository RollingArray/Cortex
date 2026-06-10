import pytest

from app.services.ai.factory import (
    get_ai_provider,
)


@pytest.mark.asyncio
async def test_ollama_chat():

    provider = get_ai_provider()

    response = await provider.generate(
        "Reply with exactly one word: Cortex"
    )

    assert response is not None

    assert len(response) > 0