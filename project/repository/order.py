from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from project import models, schemas


def show_all(db:Session):
    return db.query(models.Order).all()

def create_order(request:schemas.OrderBase,db:Session,cst_id:int):
    new_order = models.Order(order_item=request.order_item, price=request.price, customer_id=cst_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order