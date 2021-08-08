from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    class Config:
        orm_mode = True

    public_id: str
    username: str
    created: datetime
    is_active: bool


class CreateUser(BaseModel):
    username: str
    password: str


class UpdateUser(BaseModel):
    password: Optional[str]
    is_active: Optional[bool]
