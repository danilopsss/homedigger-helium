from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from helium.core.database.base import BaseModel


class UserSecrets(BaseModel):
    __tablename__ = "user_secrets"

    secret: str = Column(String, nullable=False)
    salt: str = Column(String, nullable=False)
    another_secret: str = Column(String, nullable=False)

    user_id = Column(UUID, ForeignKey("user.id"))
    user = relationship(
        "Users", lazy=True, uselist=False, back_populates="secrets"
    )
