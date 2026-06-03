from tests.conftest import get_test_client

client = get_test_client()


def test_chat_endpoint():

    response = client.post(
        "/api/v1/chat",
        json={
            "prompt": "hello"
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["success"] is True