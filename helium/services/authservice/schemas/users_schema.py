from helium.services.authservice.models import Users
from helium.core.schemas.base_schema import BaseModelSchema
from helium.services.authservice.schemas import (
    UsersDetailsSchema,
    UserAccessHistorySchema,
    UsersSecretsSchema
)


from typing import Optional


class UserSchema(BaseModelSchema):
    __dbmodel__ = Users

    username: str
    details: Optional[UsersDetailsSchema]
    secrets: Optional[UsersSecretsSchema]
    history: Optional[UserAccessHistorySchema]
