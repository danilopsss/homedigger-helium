from helium.services.authservice.models import Users
from helium.core.schemas.base_schema import BaseModelSchema
from typing import Optional, List
from helium.services.authservice.schemas.users_details_schema import (
    UsersDetailsSchema,
)
from helium.services.authservice.schemas.users_secrets_schema import (
    UsersSecretsSchema,
)
from helium.services.authservice.schemas.users_access_history import (
    UserAccessHistorySchema,
)


class UserSchema(BaseModelSchema):
    __orm_model__ = Users

    username: str
    details: Optional[UsersDetailsSchema]
    secrets: List[Optional[UsersSecretsSchema]]
    access_history: List[Optional[UserAccessHistorySchema]]
