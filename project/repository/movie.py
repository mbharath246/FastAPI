from sqlalchemy.orm import Session
from project import models, schemas
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


def show_all(db:Session):
    movie_data = db.query(models.Movie).all()
    return movie_data


def show_particular(id:int, db:Session):
    particular_movie = db.query(models.Movie).filter(models.Movie.id == id).all()
    if particular_movie:
        return particular_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="details Not Found")


def create_movie(request:schemas.Movie, db:Session):
    movie_post = models.Movie(hero=request.hero, heroin=request.heroin, director=request.director)
    db.add(movie_post)
    db.commit()
    db.refresh(movie_post)
    return movie_post


def delete_movie(id:int, db:Session):
    deleted_movie = db.query(models.Movie).filter(models.Movie.id == id).delete()
    if deleted_movie:
        db.commit()
        return {"message": "deleted sucessfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Details are not found")


def update_movie(name,new_name, db:Session):
    movie_update = db.query(models.Movie).filter(models.Movie.hero == name).first()
    if movie_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    movie_update.hero = new_name
    db.commit()
    return {"message": "updated Sucessfully"}


def update_all(id:int, request:schemas.Movie, db:Session):
    new_movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    if new_movie:
        print(new_movie.__dict__)
        print(request, request.hero, '---------------------')
        new_movie.hero = request.hero
        new_movie.director = request.heroin
        new_movie.heroin = request.director
        
        db.commit()

        return JSONResponse(content={"success": True}, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")


def update_with_dict(id:int, request:schemas.Movie, db:Session):
    new_movie = db.query(models.Movie).filter(models.Movie.id==id)
    print(new_movie,'-------------------------------------------')
    if not new_movie.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with {id} is not found")
    new_movie.update(dict(request))
    db.commit()
    return {"update":"sucessfull"}
