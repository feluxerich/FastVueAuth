from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.user import models, schemas

router = APIRouter(tags=['user'])


@router.get("/", response_model=List[schemas.User])
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/{username}", response_model=schemas.User)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db.query(models.User).filter_by(username=username).first()


@router.post("/", response_model=schemas.User)
async def create_user(db: Session = Depends(get_db)):
    if get_user_by_username("testine", db):
        # TODO set status code to 400 and
        #  tell the inform the requester that the username is already in use. ResponseSchema?
        return
    user = models.User(
        username="testine",
        password="test",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

