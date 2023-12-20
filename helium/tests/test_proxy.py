import pytest
from unittest.mock import patch
from requests.exceptions import HTTPError
from pydantic import ValidationError


def test_proxy_door_for_moria(client, response, token_response, proxy_auth_payload):
    correct_response = response(is_ok=True, response=token_response)
    with patch('requests.post', return_value=correct_response) as request_post:
        response = client.post('/gk/authenticate', json=proxy_auth_payload)
    assert response.status_code == 200
    assert response.json.get('access_token') == 'test'
    assert response.json.get('refresh_token') == 'test'
    assert request_post.called


def test_proxy_door_for_moria_with_exception(client, proxy_auth_invalid_payload):
    with pytest.raises(ValidationError) as exception:
        client.post('/gk/authenticate', json=proxy_auth_invalid_payload)
    assert exception.match('validation error for ProxyAuthSchema')
