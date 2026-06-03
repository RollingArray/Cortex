from abc import ABC
from abc import abstractmethod


class AIProvider(ABC):
    """
    Base contract for all AI providers.

    Every provider implementation must expose
    a common generate() interface.
    """

    @abstractmethod
    async def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the provider.

        Args:
            prompt: User prompt

        Returns:
            Generated response text
        """
        raise NotImplementedError