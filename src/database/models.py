from pydantic import BaseModel


class Movie(BaseModel):
    hero: str
    heroin:str
    moviename:str


class User(BaseModel):
    id: int
    fullname: str
    username: str
    is_active: bool

class UserIn(User):
    hash_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None