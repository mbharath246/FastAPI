from fastapi import APIRouter, Depends, HTTPException, status
from src.database.connection import get_db
from sqlalchemy.orm import Session
from src.database import models, schemas
from src.auth import hashing


router = APIRouter(
    tags=["Users"],
    prefix="/user"
)


@router.get("/")
def get_all_users(db:Session = Depends(get_db)):
    return db.query(schemas.User).all()

@router.post("/create")
def create_user(request: models.UserIn, db:Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="username already exists")
    new_user = schemas.User(fullname=request.fullname, username=request.username,  hash_password=hashing.get_hash_password(request.hash_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
