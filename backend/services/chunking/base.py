from abc import ABC
from abc import abstractmethod

from backend.services.documents.models import Document


class Chunker(ABC):

    @abstractmethod
    def chunk(
        self,
        document: Document,
    ):
        pass