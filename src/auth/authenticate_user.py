from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.database import models, schemas
from src.database.connection import get_db
from src.auth import hashing, token


router = APIRouter(
    tags=["Authenticate"],
)


@router.post("/token")
def verify_login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Login Credentials")
    if not hashing.verify_hash_password(request.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Passowrd")
    
    jwt_token = token.create_access_token({"uname":user.username})

    return models.Token(access_token = jwt_token, token_type = "Bearer")