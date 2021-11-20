# imports:
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# instead of table - we will create classes
from sqlalchemy.ext.declarative import declarative_base

# instead of connection

from sqlalchemy.orm import sessionmaker

# execute instructions from "chinook" database

db = create_engine("postgresql:///chinook")
base = declarative_base


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# session will create new instance of sessionmaker
# than point to engine (db) instead of connect

Session = sessionmaker(db)

# opens instance, by calling the Session() subclass created above

session = Session()