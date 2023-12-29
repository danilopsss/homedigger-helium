import pytest
from unittest.mock import patch
from helium.core.utils.secrets import Secrets
from helium.core.utils.filehelpers import load_config_from_file
from helium.core.utils.token import generate_general_token, retrieve_session_token, verify_token, verify
from helium.services.authservice.schemas import (
    UsersSecretsSchema,
)
from helium.core.utils.token.exceptions import ExpiredAccessToken, ExpiredRefreshToken


@patch("tomllib.load")
def test_load_config_from_file(load, some_file):
    load.return_value = {"test": {"test": "test"}}
    assert load_config_from_file(some_file, "test") == {"test": "test"}
    assert load.called


def test_secrets():
    secret_schema = UsersSecretsSchema(secret="mysecret")
    secrets = Secrets(secrets=secret_schema.model_dump())
    assert type(secrets.generate_random_bytes) == bytes
    generated_secret = secrets.process_secret().get("secrets")
    assert set(generated_secret.keys()).intersection({"salt", "secret", "another_secret"})


def test_compare_passwords(hashed_password):
    user_mocked = UsersSecretsSchema(
        secret="passwd1",
        salt="12345salt",
    )
    user_hash = Secrets(user_mocked.model_dump()).hash_password()
    assert hashed_password == user_hash


def test_generation_token_generation(user_from_db):
    jwt = generate_general_token(user_from_db)
    assert jwt is not None
    assert len(jwt.split(".")) == 3


def testretrieve_session_token(user_from_db):
    jwt = retrieve_session_token(user_from_db)
    assert jwt is not None
    assert len(jwt.get("access_token").split(".")) == 3
    assert len(jwt.get("refresh_token").split(".")) == 3
    assert jwt.get("access_token") != jwt.get("refresh_token")


def test_valid_token_verification(user_from_db):
    jwt = retrieve_session_token(user_from_db)
    assert verify_token(user_from_db, jwt)

    jwt = retrieve_session_token(user_from_db, exp=-1)
    with pytest.raises((ExpiredAccessToken, ExpiredRefreshToken)) as exc:
        verify_token(user_from_db, jwt)
    assert exc.type in (ExpiredAccessToken, ExpiredRefreshToken)


def test_invalid_token_verification(user_from_db):
    jwt = retrieve_session_token(user_from_db, exp=-1)
    key = user_from_db.secrets.personal_key

    with pytest.raises(ExpiredAccessToken) as exc:
        verify(jwt, "access_token", key[len(key) // 2 :])
    assert exc.type == ExpiredAccessToken

    with pytest.raises(ExpiredRefreshToken) as exc:
        verify(jwt, "refresh_token", key[len(key) // 2 :])
    assert exc.type == ExpiredRefreshToken
