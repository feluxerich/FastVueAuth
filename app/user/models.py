from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True)
    password = Column(String(255))
    created = Column(Date, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
