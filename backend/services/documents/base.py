from abc import ABC
from abc import abstractmethod

from backend.services.documents.models import Document


class DocumentLoader(ABC):

    @abstractmethod
    def load(
        self,
        path: str,
    ) -> Document:
        pass