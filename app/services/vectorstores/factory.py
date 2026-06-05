from app.services.vectorstores.mock import (
    MockVectorStore,
)


_store = MockVectorStore()


def get_vector_store():

    return _store