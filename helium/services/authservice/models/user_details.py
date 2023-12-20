from sqlalchemy.orm import relationship
from helium.core.database.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime, ForeignKey


class UserDetails(BaseModel):
    __tablename__ = "user_details"

    name: String = Column(String(100), nullable=False, index=True)
    birthday: DateTime = Column(DateTime, nullable=False)
    email: String = Column(String(100), nullable=False, index=True, unique=True)

    user_id = Column(UUID, ForeignKey("user.id", ondelete="NO ACTION"))
    user = relationship("Users", lazy=True, uselist=False, back_populates="user_details")
