from fastapi import APIRouter, Depends, status
from ..import database, models, schemas
from sqlalchemy.orm import Session
from fastapi.responses import Response
from project.repository import movie
from project import oauth2


router = APIRouter(
    prefix="/movie",
    tags=["Movie"]
)

get_db = database.get_db

# get a Movie Details
@router.get('/')
def show_movie(db: Session = Depends(get_db), current_user:schemas.UserIn = Depends(oauth2.get_current_user)):
    return movie.show_all(db)


# get the details with path
@router.get('/particular/{id}')
def movie_id(id: int, db:Session=Depends(get_db)):
    return movie.show_particular(id,db)


# Store the details in a database
@router.post('/create', response_model = schemas.ShowMovie ,status_code=status.HTTP_201_CREATED)
def movie_create(request: schemas.Movie,  db: Session=Depends(get_db)):
    return movie.create_movie(request=request, db=db)


# delete the data in a database
@router.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def movie_delete(id, db: Session=Depends(get_db)):
   return movie.delete_movie(id=id, db=db)


# update the data in a database
@router.put('/update/{name}', status_code=status.HTTP_201_CREATED)
def movie_put(name,new_name, db:Session = Depends(get_db)):
    return movie.update_movie(name=name, new_name=new_name,db=db)


# ------OR-----
@router.put('/update2/{id}',status_code=status.HTTP_202_ACCEPTED)
def put_movie(id, request:schemas.Movie, db:Session=Depends(get_db)):
    return movie.update_all(id,request,db)

# RESPONSE MODEL
@router.get('/get/response/{id}')
def get_movie(id: int, response:Response, db:Session = Depends(get_db)):
    movie_details = db.query(models.Movie).filter(models.Movie.id == id).all()
    if movie_details:
        return movie_details
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"details":f'movie id with {id} is not present'}


# UPDATE
@router.put('/update/dict/{id}')
def movie_update(id, request:schemas.Movie, db:Session = Depends(get_db)):
    return movie.update_with_dict(id,request,db)
