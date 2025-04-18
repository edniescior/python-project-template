from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from {{ cookiecutter.package_slug }}.main import app


@pytest.fixture(name='client')
def _client():
    return TestClient(app)


def test_hello(client):
    """
    Root URL greets the world.
    """
    resp = client.get('/')

    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Hello': 'World'}
