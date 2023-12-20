from pydantic import BaseModel


class Credentials(BaseModel):
    username: str
    password: str


class ProxyAuthSchema(BaseModel):
    door: str
    keychain: str
    credentials: Credentials


class ProxyAuthSchemaResponse(BaseModel):
    access_token: str
    refresh_token: str
