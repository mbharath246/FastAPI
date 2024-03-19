from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from project import models, database
from fastapi import Depends, HTTPException, status
from project.hash import hash_verify
from project.routers import JWTtoken


router = APIRouter(
    tags=["Autentication"]
)

@router.post('/token')
def user_login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    if not hash_verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect password')
    
    # GENERATE A JWT TOKEN AND RETURN IT
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}