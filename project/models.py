from sqlalchemy import Boolean, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from project.database import Base

class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, index=True)
    hero = Column(String, nullable=False)
    director = Column(String, nullable=False)
    heroin = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phno = Column(String)
    address = Column(String)
    password = Column(String)

    ord = relationship("Order", back_populates="cst")

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    order_item = Column(String)
    price = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    cst = relationship("Customer", back_populates="ord")