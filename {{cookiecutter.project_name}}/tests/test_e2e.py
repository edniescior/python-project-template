import pytest

from hello_svc.main import app
from fastapi.testclient import TestClient

@pytest.fixture(name="client")
def _client():
    return TestClient(app)

def test_hello(client):
    """
    Root URL greets the world.
    """
    resp = client.get("/")

    assert 200 == resp.status_code
    assert {
        "Hello": "World"
    } == resp.json()
