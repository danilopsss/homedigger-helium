from unittest.mock import patch
from helium.core.utils.secrets import Secrets
from helium.core.utils.filehelpers import load_config_from_file
from helium.services.authservice.schemas.users_secrets_schema import (
    UsersSecretsSchema,
)


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
    assert set(generated_secret.keys()).intersection(
        {"salt", "secret", "another_secret"}
    )


def test_compare_passwords():
    hashed_password = (
        "f02d517e028ec808cfd86b9bdd8ced"
        "961259610b56be781c17de2a54ec40e"
        "051f3467fd78ea877db34e4c38f1758"
        "f1d3c6df0650aeb1806e45174f31622f53a1"
    )
    user_mocked = UsersSecretsSchema(
        secret="passwd1",
        salt="12345salt",
    )
    user_hash = Secrets(user_mocked.model_dump()).hash_password()
    assert hashed_password == user_hash
