from helium.core.schemas.base_schema import BaseModelSchema
from helium.services.authservice.models import UserAccessHistory, Events


class UserAccessHistorySchema(BaseModelSchema):
    __orm_model__ = UserAccessHistory

    event: Events
    ip: str
    user_agent: str
