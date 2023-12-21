from helium.core.schemas.base_schema import BaseModelSchema
from helium.services.authservice.models import UserSecrets


class UsersSecretsSchema(BaseModelSchema):
    __dbmodel__ = UserSecrets

    secret: str
