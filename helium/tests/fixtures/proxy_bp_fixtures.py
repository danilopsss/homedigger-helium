import pytest


@pytest.fixture
def proxy_auth_payload():
    return {
        "door": "durin",
        "keychain": "moria",
        "credentials": {
            "username": "gandalf",
            "password": "mellon"
        }
    }

@pytest.fixture
def proxy_auth_invalid_payload(proxy_auth_payload):
    proxy_auth_payload.pop('credentials')
    return proxy_auth_payload
