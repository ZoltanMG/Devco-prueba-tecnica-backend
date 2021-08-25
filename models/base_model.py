#!/usr/bin/python3
from uuid import uuid4
import models
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

# Base es la instancia del ORM
Base = declarative_base()


class BaseModel:
    """
    las clases Postulante y Question heredan de BaseModel
    """
    id = Column(String(60), nullable=False, primary_key=True)

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        """
        Genera un diccionario con los atributos de los objetos.
        """
        tmp_dict = self.__dict__
        copy_dict = tmp_dict.copy()
        if "_sa_instance_state" in copy_dict:
            del copy_dict['_sa_instance_state']
        return copy_dict

    def save(self):
        """
        Guarda el objeto
        """
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """
        Elimina el objeto
        """
        models.storage.delete(self)
