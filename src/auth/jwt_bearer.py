from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.auth.token import verify_access_token


# class JwtBearer(HTTPBearer):
#     def __init__(self,auto_Error: bool = True):
#         super(JwtBearer, self).__init__(auto_error=auto_Error)

    
#     async def __call__(self, request: Request):
#         credentials : HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)

#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or Expire Token")
#             if self.verify_jwt(credentials.credentials):
#                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Token or Expired Token")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or Expire Token")

        
#     def verify_jwt(self, jwtoken : str):
#         isTokenValid : bool = False
        
#         payload = verify_access_token(jwtoken)
#         if payload:
#             isTokenValid = True
#         return isTokenValid
    


class JwtBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auto_error = self.auto_error
        credentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid or Expired Token")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid or Expired Token")
            return credentials.credentials
        else:
            if auto_error:
                raise HTTPException(status_code=403, detail="Invalid or Expired Token")
            return None

    def verify_jwt(self, jwtoken: str):
        payload = verify_access_token(jwtoken)
        if payload:
            return True
        return False

