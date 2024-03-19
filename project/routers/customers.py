from fastapi import APIRouter, Depends
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from project.repository import customer

router = APIRouter(
    prefix="/customer",
    tags=["Customers"]
)

get_db = database.get_db

""" RELATIONSHIPS OF CUSTOMERS AND ORDERS """
# GET ALL CUSTOMERS
@router.get('/get', response_model=List[schemas.CustomerOut])
def all_customers(db:Session = Depends(get_db)):
    return customer.show_all(db)

# CREATE CUSTOMER DETAILS
@router.post('/create/details', response_model=schemas.CustomerBase)
def create_customers(request: schemas.CustomerIn, db:Session = Depends(get_db)):
    return customer.create_customer_details(request, db)