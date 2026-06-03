from abc import ABC
from abc import abstractmethod


class AIProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
    ) -> str:
        pass