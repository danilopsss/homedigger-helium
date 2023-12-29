import pytest
from helium.services.authservice.models import Users
from helium.services.authservice.models import UserSecrets


@pytest.fixture
def hashed_password():
    return (
        "f02d517e028ec808cfd86b9bdd8ced"
        "961259610b56be781c17de2a54ec40e"
        "051f3467fd78ea877db34e4c38f1758"
        "f1d3c6df0650aeb1806e45174f31622f53a1"
    )


@pytest.fixture
def another_secret():
    return (
        "X501MRZFyEjpXhZQTHHcvKeFHT84CDvYdtjlVxaH"
        "e9FrH8wyNFWuj+e5nNQkwBrxFWNTGfJpYsJu4HXd9"
        "qKz3va168nARmkRmyPDJ0OOFqDqBJ/SzX6y9YxgKq"
        "VAbIfbJYZAjP91MlKI3Irugh9n2LjhHYAxqc39yy6pUzsOCbo"
    )


@pytest.fixture
def user_from_db(hashed_password, another_secret):
    return Users(
        username="johndoe@example.com", secrets=UserSecrets(secret=hashed_password, personal_key=another_secret)
    )
