from enum import Enum as PyEnum
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from helium.core.database.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID


class Events(PyEnum):
    TOKEN_GENERATED = "TOKEN_GENERATED"
    TOKEN_REFRESHED = "TOKEN_REFRESHED"


class UserAccessHistory(BaseModel):
    __tablename__ = "user_access_history"

    event: String = Column(Enum(Events), nullable=False, index=True)
    ip: String = Column(String, nullable=False)
    user_agent: String = Column(String(100), nullable=False, index=True, unique=True)

    user_id = Column(UUID, ForeignKey("user.id", ondelete="NO ACTION"))
    user = relationship("Users", lazy=True, uselist=False, back_populates="user_access_history")
