from app.services.documents.text_loader import (
    TextLoader,
)


def test_text_loader():

    loader = TextLoader()

    document = loader.load(
        "data/sample/cortex.txt"
    )

    assert (
        "Cortex"
        in document.content
    )