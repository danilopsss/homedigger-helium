import requests
from flask import jsonify, current_app
from requests.exceptions import HTTPError
from gatekeeper.services.proxy.authservice.schemas import ProxyAuthSchema


def get_authserver_url() -> str:
    if not (url := current_app.config.get("MORIA_URL")):
        raise ValueError("MORIA_URL is not set in the config")
    if not (port := current_app.config.get("MORIA_PORT")):
        raise ValueError("MORIA_PORT is not set in the config")
    if not (version := current_app.config.get("MORIA_API_VERSION")):
        raise ValueError("MORIA_API_VERSION is not set in the config")
    return f"{url}:{port}/{version}/authenticate"


def validate_response(response: requests.Response) -> bool:
    json_response = response.json()
    if not (
        response.ok and
        json_response.get("access_token") and
        json_response.get("refresh_token")
    ):
        raise HTTPError("Invalid response from the auth server")


def get_token(url: str, credentials: dict) -> dict:
    try:
        response = requests.post(url, json=credentials)
        validate_response(response)
        return response.json()
    except ValueError as value_error:
        raise value_error
    except HTTPError as http_error:
        raise http_error


def authenticate(remote_url: str, data: ProxyAuthSchema):
    return jsonify(get_token(remote_url, data.credentials))
