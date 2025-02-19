import pytest
from helium import app
from datetime import datetime


@pytest.fixture(autouse=True)
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def mocked_secrets():
    return {"secret": "my_very_secret_secret"}


@pytest.fixture(autouse=True)
def mocked_user_details():
    return {
        "name": "John Doe",
        "birthday": datetime(1990, 1, 1).timestamp(),
        "email": "johnd@provider.com",
    }


@pytest.fixture(autouse=True)
def mocked_user(mocked_user_details, mocked_secrets):
    return {
        "username": "johnd",
        "details": mocked_user_details,
        "secrets": mocked_secrets,
    }
