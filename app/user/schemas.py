from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    class Config:
        orm_mode = True

    username: str
    created: date
    is_active: bool


class CreateUser(BaseModel):
    username: str
    password: str
