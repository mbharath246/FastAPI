from src.database.connection import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    username = Column(String, unique=True)
    is_active = Column(Boolean, default=False)
    hash_password = Column(String, nullable=False)


class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    hero = Column(String)
    heroin = Column(String)
    moviename = Column(String)


