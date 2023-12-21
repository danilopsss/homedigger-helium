from helium.core.schemas.base_schema import BaseModelSchema
from helium.services.authservice.models import UserDetails
from datetime import datetime
from pydantic import EmailStr


class UsersDetailsSchema(BaseModelSchema):
    __dbmodel__ = UserDetails

    name: str
    birthday: datetime
    email: EmailStr
