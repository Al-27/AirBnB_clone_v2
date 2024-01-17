#!/usr/bin/python3
"""
docs
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session,scoped_session, sessionmaker
import MySQLdb
from os import environ
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

CLASSES = [State,User, City,Review,Amenity,Place ]

class DBStorage:
    """ """
    
    __engine = None
    __session = None
    
    def __init__(self):
        """
        """
        self.__engine = create_engine(f"mysql+mysqldb://{environ.get('HBNB_MYSQL_USER')}:{environ.get('HBNB_MYSQL_PWD')}@localhost/{environ.get('HBNB_MYSQL_DB')}",pool_pre_ping=True)
               
        if environ.get('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
    
    def new(self, obj):
        """
        """
       # obj.__delattr__("_sa_instance_state")
        self.__session.add(obj)
        
    def delete(self, obj=None):
        """
        """
        if obj is not None:
            self.__session.delete(obj)
    
    def save(self):
        """
        """
        self.__session.commit()
    
    def all(self, cls=None):
        """
        """
        dict_obj = {}
        
        if cls is not None:            
            for _cls in self.__session.query(cls).all():
                key = "{}.{}".format(_cls.__class__.__name__ ,_cls.id )
                dict_obj[key] = _cls.to_dict()
        else:
            for Class in CLASSES:
                for _cls in self.__session.query(Class).all():
                    key = "{}.{}".format(_cls.__class__.__name__ ,_cls.id )
                    dict_obj[key] = _cls.to_dict()
        
        return dict_obj
    
    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(self.__engine,expire_on_commit=False))