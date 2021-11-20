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

# session will create new instance of sessionmaker
# than point to engine (db) instead of connect

Session = sessionmaker(db)

# opens instance, by calling the Session() subclass created above

session = Session()