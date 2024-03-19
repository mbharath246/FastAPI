from project import models, schemas
from sqlalchemy.orm import Session

def show_all(db:Session):
    customers_details = db.query(models.Customer).all()
    return customers_details

def create_customer_details(request:schemas.CustomerIn, db:Session):
    new_customer = models.Customer(name=request.name, phno=request.phno, address=request.address, password=request.password)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
