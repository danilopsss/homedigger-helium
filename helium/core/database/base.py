from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import validates, as_declarative
from sqlalchemy.dialects.postgresql import UUID


@as_declarative()
class BaseModel:
    __abstract__ = True

    id = Column(UUID, primary_key=True, nullable=False, default=uuid4)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @validates('created')
    def validate_created(self):
        return self.created
