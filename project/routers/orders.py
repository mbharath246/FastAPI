from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, models
from project.repository import order


router = APIRouter(
    prefix="/order",
    tags=["Orders"]
)

get_db = database.get_db


# GET ALL ORDERS
@router.get('/get', response_model=list[schemas.OrderGet])
def all_orders(db:Session = Depends(get_db)):
    return order.show_all(db=db)


# CREATE ORDERS DETAILS
@router.post('/create')
def create_orders(*,request:schemas.OrderBase, db: Session = Depends(get_db), cst_id:int):
    return order.create_order(request=request,db=db,cst_id=cst_id)