#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import Base
from models.postulante import Postulante
from models.question import Question
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
"""
Aquí se realiza la conexión entre MySql y Klask a través del ORM sqlalchemy 
"""

# Este es un diccionario con todas las clases.
clases = {"Postulante": Postulante, "Question": Question}


class DBStorage:
    """
    Con esta clase se gestionará los querys de la base de datos.
    """
    __engine = None
    session = None

    def __init__(self):
        """
        los datos para la coneccion con la base de datos es a 
        través de variables de entorno para mayor seguridad
        """
        USER_MYSQL = getenv('USER_MYSQL')
        PWD_MYSQL = getenv('PWD_MYSQL')
        HOST_MYSQL = getenv('HOST_MYSQL')
        DB_MYSQL = getenv('DB_MYSQL')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER_MYSQL,
                                             PWD_MYSQL,
                                             HOST_MYSQL,
                                             DB_MYSQL), pool_size=20, max_overflow=0)

    def new(self, objeto):
        self.session.add(objeto)

    def save(self):
        """
        con este método se guardan los objetos en la base de datos
        """
        self.session.commit()

    def delete(self, objeto=None):
        """
        con este método se eliminan los objetos en la base de datos
        """
        if objeto is not None:
            self.session.delete(objeto)

    def reload(self):
        """
        con este método se cargan los objetos en la base de datos
        """
        Base.metadata.create_all(self.__engine)
        sesion_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesion_factory)
        self.session = Session
