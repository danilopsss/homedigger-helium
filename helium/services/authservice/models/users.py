from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from helium.core.database.base import BaseModel


relation_config = {
    "uselist": False,
    "back_populates": "user",
    "cascade": "all, delete-orphan",
}


class Users(BaseModel):
    __tablename__ = "user"

    username: String = Column(
        String(100), nullable=False, index=True, unique=True
    )

    details = relationship("UserDetails", **relation_config)
    secrets = relationship("UserSecrets", **relation_config)
    access_history = relationship("UserAccessHistory", **relation_config)
