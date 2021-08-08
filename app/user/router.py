from typing import List

from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from passlib.context import CryptContext
from starlette import status
from starlette.responses import Response

from app.database import get_db
from app.user import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(tags=['User'])


# TODO add admin decorator (after auth has been implemented)


@router.get("/", response_model=List[schemas.User], name='Admins can get a list of all user accounts')
async def get_all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/{public_id}", response_model=schemas.User, name='Admins can get a user account')
async def get_user(public_id: str, db: Session = Depends(get_db)):
    return db.query(models.User).filter_by(public_id=public_id).first()


@router.get("/me", response_model=schemas.User, name='User can see their account information')
async def get_user(public_id: str, db: Session = Depends(get_db)):
    # TODO
    # return db.query(request.user).filter_by(public_id=public_id).first()
    pass


@router.post("/", response_model=schemas.User, name='Admins can create user accounts')
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    if db.query(models.User).filter_by(username=user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username already in use')
    user = models.User(
        username=user.username,
        password=pwd_context.hash(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{public_id}", response_model=schemas.User, name='Admins can update accounts')
async def update_user(public_id: str, updates: schemas.UpdateUser, db: Session = Depends(get_db)):
    if not (user := await get_user(public_id, db)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # indicates that the user (not the admin!) has deleted the account
    user.is_active = updates.is_active

    if updates.password:
        user.password = pwd_context.hash(updates.password)

    db.add(user)
    db.commit()
    return user


@router.put("/me", response_model=schemas.User, name='User can update their own account')
async def update_user_self(updates: schemas.UpdateUser, db: Session = Depends(get_db)):
    # TODO user = request.user
    user = None
    user.is_active = updates.is_active

    if updates.password:
        user.password = pwd_context.hash(updates.password)

    db.add(user)
    db.commit()
    return None


@router.delete("/{public_id}", name='Admins can delete user accounts', status_code=status.HTTP_200_OK)
async def delete_user(public_id: str, db: Session = Depends(get_db)):
    if user := await get_user(public_id, db):
        db.delete(user)
        db.commit()
    return Response("Deleted")
