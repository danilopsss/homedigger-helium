from helium.core.schemas.base_schema import BaseModelSchema
from helium.services.authservice.models import UserDetails


class UsersDetailsSchema(BaseModelSchema):
    __orm_model__ = UserDetails

    name: str
    birthday: int
    email: str
