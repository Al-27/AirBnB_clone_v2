#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from sqlalchemy import *
from sqlalchemy.orm import relationship 
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column( String(128), nullable=False)
    
    cities = relationship('City', backref='state',cascade="all, delete, delete-orphan")
    
    from os import environ as env
    if env.get("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            _cities = models.storage.all(City).copy()
            cits = []
            for cit in _cities.values():
                if( cit.state_id == self.id ):
                    cits.append(cit)
            return cits