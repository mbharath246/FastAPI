from sqlalchemy.orm import Session
from project import models, schemas
from fastapi import HTTPException, status
from project.hash import hashed


def show_all_users(db:Session):
    return db.query(models.User).all()


def get_particular_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} not found")
    return user

def create_user(request:schemas.UserIn, db:Session):
    hash_password = hashed(request.password)
    new_user = models.User(name=request.name, email=request.email,password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request


def delete_user(id:int, db:Session):
    remove_user = db.query(models.User).filter(models.User.id == id)
    if not remove_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'the user with id: {id} is not found')
    remove_user.delete()
    db.commit()
    return {"message":f"user with id:{id} deleted Successfully"}


def update_user(id:int, request:schemas.UserIn, db:Session):
    update_user = db.query(models.User).filter(models.User.id == id).first()
    password = hashed(request.password)
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'the user with id: {id} is not found')

    update_user.email = request.email
    update_user.password = password

    db.commit()
    return {"message":"update successfully"}