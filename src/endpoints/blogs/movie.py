from fastapi import APIRouter, Depends, HTTPException, status
from src.database.connection import get_db
from sqlalchemy.orm import Session
from src.database import models, schemas
from src.auth.jwt_bearer import JwtBearer
# from src.auth.token import verify_access_token

router = APIRouter(
    tags=["Movie"],
    prefix="/movie",
    dependencies=[Depends(JwtBearer())]
)

@router.get("/")
def get_all_movies(db:Session = Depends(get_db)):
    return db.query(schemas.Movie).all()

@router.post("/create")
def create_movie_details(request: models.Movie, db:Session = Depends(get_db)):
    movie = db.query(schemas.Movie).filter(schemas.Movie.moviename == request.moviename).first()
    if movie:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="moviename already exists")
    new_movie = schemas.Movie(hero=request.hero, heroin=request.heroin,  moviename=request.moviename)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
