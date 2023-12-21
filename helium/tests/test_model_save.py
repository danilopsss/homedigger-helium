import pytest


@pytest.mark.usefixtures('client')
def test_user_register(client, mocked_user):
    response = client.post("/api/v1/auth/register", json=mocked_user)
    assert response.status_code == 201
    assert response.json == {
        "username": mocked_user.get("username"),
        "status": "created"
    }
