import jwt
from datetime import datetime, timedelta


def generate_jwt_token(user):
    jwt.encode(
        {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(minutes=15),
        },
        "secret",
        algorithm="HS256",
    )
    # return token.encode(
    #     {
    #         "username": user.username,
    #         "email": user.email,
    #         "role": user.role,
    #         "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
    #     },
    #     "secret",
    #     algorithm="HS256",
    # )
