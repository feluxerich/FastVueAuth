import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import DateTime
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    public_id = Column(String(36), unique=True)
    username = Column(String(64), unique=True)
    password = Column(String(255))
    created = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO verify that the public id does not exist yet
        self.public_id = str(uuid.uuid4())
