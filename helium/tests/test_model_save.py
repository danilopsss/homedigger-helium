import pytest
from unittest.mock import patch
from helium.services.utils.api_types import ApiResponse


@pytest.mark.usefixtures("client")
@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.commit")
def test_user_register(commit, create_engine, client, mocked_user):
    response = client.post("/api/v1/auth/register", json=mocked_user)
    assert commit.called
    assert create_engine.called
    assert response.status_code == 201
    assert response.json == {
        "user": mocked_user.get("username"),
        "status": ApiResponse.CREATED.message,
    }
