from typing import Any


def test_health_returns_ok(client: Any):

    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
