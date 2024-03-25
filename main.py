from fastapi import FastAPI
from src.database import models, schemas

from src.endpoints.user import user_details
from src.endpoints.blogs import movie
from src.database.connection import engine
from src.auth import authenticate_user

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authenticate_user.router)
app.include_router(user_details.router)
app.include_router(movie.router)