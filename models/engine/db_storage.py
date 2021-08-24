#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import Base
from models.postulante import Postulante
from models.question import Question
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

clases = {"Postulante": Postulante, "Question": Question}

class DBStorage:
    __engine = None
    session = None

    def __init__(self):
        USER_MYSQL = getenv('USER_MYSQL')
        PWD_MYSQL = getenv('PWD_MYSQL')
        HOST_MYSQL = getenv('HOST_MYSQL')
        DB_MYSQL = getenv('DB_MYSQL')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER_MYSQL,
                                             PWD_MYSQL,
                                             HOST_MYSQL,
                                             DB_MYSQL), pool_size=20, max_overflow=0)

    def all(self, cls=None):
        new_dict = {}
        for clase in clases:
           objetos = self.session.queery(clases[clase]).all()
           for objeto in objetos:
               key = objeto.__class__.__name__ + '.' + objeto.id
               new_dict[key] = objeto 
        return new_dict

    
    def new(self, objeto):
        self.session.add(objeto)

    def save(self):
        self.session.commit()

    def delete(self, objeto=None):
        if objeto is not None:
            self.session.delete(objeto)

    def reload(self):

        Base.metadata.create_all(self.__engine)
        sesion_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesion_factory)
        self.session = Session
