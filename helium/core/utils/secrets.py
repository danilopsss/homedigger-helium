from os import urandom
from random import randint
from base64 import b64encode
from hashlib import pbkdf2_hmac


class Secrets:
    def __init__(self, secrets: dict):
        self._secrets = {key: bytes(value.encode("utf-8")) for key, value in secrets.items()}

    @property
    def secret(self):
        return self._secrets

    @property
    def generate_random_bytes(self):
        return urandom(randint(128, 512))

    @property
    def _salt(self):
        if not self.secret.get("salt"):
            self.secret["salt"] = b64encode(self.generate_random_bytes)
        return b64encode(self.secret.get("salt"))

    @property
    def _another_secret(self):
        if not self.secret.get("another_secret"):
            self.secret["another_secret"] = b64encode(self.generate_random_bytes)
        return b64encode(self.secret.get("another_secret"))

    def hash_password(self):
        password = bytes(self.secret.get("secret", ""))
        return pbkdf2_hmac(
            hash_name="SHA512",
            password=password,
            salt=self._salt,
            iterations=(1024 * 1024),
        ).hex()

    def process_secret(self) -> dict:
        password = self.hash_password()
        return {
            "secrets": {
                "salt": self._salt,
                "secret": password,
                "personal_key": self._another_secret,
            }
        }
