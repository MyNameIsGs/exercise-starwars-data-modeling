import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(90))
    password = Column(String(90))

    



class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birthday = Column(String(80), nullable=False)
    color_eyes = Column(String(50), nullable=False)
    color_hair = Column(String(50), nullable=False)
    tone_skin = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    poblation = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    passengers = Column(String(250))
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    character_id = Column(Integer, ForeignKey("character.id"))
    planets_id = Column(Integer, ForeignKey("planets.id"))
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')