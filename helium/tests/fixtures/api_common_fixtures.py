import pytest
from gatekeeper import app


class MockedResponse:
    def __init__(self, is_ok: bool, response: dict):
        self.resp = response
        self.is_ok = is_ok
    def ok(self): return self.is_ok
    def json(self): return self.resp


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def response():
    def _response(is_ok: bool, response: dict):
        return MockedResponse(is_ok, response)
    return _response


@pytest.fixture
def token_response():
    return {
        "access_token": "test",
        "refresh_token": "test"
    }
