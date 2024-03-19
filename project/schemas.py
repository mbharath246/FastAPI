from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    hero: str
    heroin: str
    director: str

    class Config:
        from_attributes = True

class ShowMovie(BaseModel):
    director: str

    class Config:
        from_attributes = True

# USER OUTPUT
class UserOut(BaseModel):
    id: int
    name: str
    email: str

# USER INPUT
class UserIn(UserOut):
    password: str


''''CUSTOMERS AND ORDERS RELATIONSHIP'''

# BASE ORDERS
class OrderBase(BaseModel):
    order_item: str
    price: int

    # class Config:
    #     orm_mode = True

# BASE CUSTOMERS
class CustomerBase(BaseModel):
    name: str
    phno: int
    address: str


class CustomerIn(CustomerBase):
    password: str


class CustomerOut(CustomerBase):
    ord: List[OrderBase]

    # class Config:
    #     orm_mode = True

class OrderGet(OrderBase):
    cst: CustomerBase


# LOGIN
class Login(BaseModel):
    username: str
    password: str



# TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None