from fastapi import FastAPI
from project.database import engine
from project import models
from project.routers import customers, orders, users, movie, login

app=FastAPI()

app.include_router(login.router)
app.include_router(customers.router)
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(movie.router)


models.Base.metadata.create_all(bind=engine)
