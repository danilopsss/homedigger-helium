from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from helium.core.database.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID


class UserSecrets(BaseModel):
    __tablename__ = "user_secrets"

    secret: str = Column(String, nullable=False)

    user_id = Column(UUID, ForeignKey("user.id", ondelete="NO ACTION"))
    user = relationship("Users", lazy=True, uselist=False, back_populates="user_secrets")
