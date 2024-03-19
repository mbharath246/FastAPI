from fastapi import Depends, HTTPException, status
from project.routers import JWTtoken
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

''' the token_url="token" referes to the router path url of login.py --->  ''' # @router.post('/token'))



def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    
    return JWTtoken.verify_token(token, credentials_exception)
