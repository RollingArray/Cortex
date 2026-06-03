from tests.conftest import get_test_client


client = get_test_client()


def test_health_endpoint():

    response = client.get(
        "/api/v1/health"
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["success"] is True
    assert payload["status"] == "healthy"


def test_ready_endpoint():

    response = client.get(
        "/api/v1/ready"
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["success"] is True
    assert payload["status"] == "ready"


def test_info_endpoint():

    response = client.get(
        "/api/v1/info"
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["success"] is True

    assert "application" in payload
    assert "version" in payload
    assert "environment" in payload