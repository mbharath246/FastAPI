from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database
from sqlalchemy.orm import Session
from project.hash import hashed
from project.repository import user

router = APIRouter(
    prefix='/users',
    tags=["Users"]
)

get_db = database.get_db


# SHOW ALL USERS
@router.get('/', response_model=list[schemas.UserOut])
def get_all_users(db:Session = Depends(get_db)):
    return user.show_all_users(db)


# SHOW PARTICULAR USER
@router.get('/particular/{id}', response_model=schemas.UserIn)
def show_user(id: int,db:Session =Depends(get_db)):
    return user.get_particular_user(id,db)


# CREATE USER
@router.post('/create', response_model=schemas.UserOut)
def create_user(request: schemas.UserIn, db: Session = Depends(get_db)):
    return user.create_user(request,db)


# DELETE USER
@router.delete('/delete/{id}')
def delete_user(id: int, db:Session = Depends(get_db)):
    return user.delete_user(id,db)

# UPDATE USER
@router.put('/update/{id}')
def user_update(id, request:schemas.UserIn ,db:Session = Depends(get_db)):
    return user.update_user(id, request,db)