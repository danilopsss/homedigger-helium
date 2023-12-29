import jwt
from datetime import datetime, timedelta
from helium.services.authservice.models.users import Users
from .exceptions import ExpiredAccessToken, ExpiredRefreshToken


def generate_general_token(user: Users, exp: int = 15):
    key = user.secrets.personal_key
    return jwt.encode(
        payload={
            "username": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=exp),
        },
        key=key[len(key) // 2 :],
        algorithm="HS512",
    )


def retrieve_session_token(user: Users, exp: int = 5):
    return {
        "access_token": generate_general_token(user, exp=exp),
        "refresh_token": generate_general_token(user, exp=exp * 3),
    }


def verify(token_pair: dict, token_name: str, key: str):
    token = token_pair.get(token_name)
    try:
        jwt.decode(token, verify=True, algorithms=["HS512"], key=key)
    except jwt.ExpiredSignatureError:
        raise {
            "access_token": ExpiredAccessToken,
            "refresh_token": ExpiredRefreshToken,
        }.get(token_name)


def verify_token(user: Users, token_pair: dict):
    key = user.secrets.personal_key
    try:
        verify(token_pair, "access_token", key[len(key) // 2 :])
        verify(token_pair, "refresh_token", key[len(key) // 2 :])
    except ExpiredAccessToken:
        raise ExpiredAccessToken()
    except ExpiredRefreshToken:
        raise ExpiredRefreshToken()
    return True
