#!/usr/bin/python3
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.question import Question
from models.base_model import Base
from sqlalchemy import Column, String


class Postulante(BaseModel, Base):
    """
    la clase que almacena toda la información de los postulanes
    """
    __tablename__ = 'postulantes'
    name = Column(String(80), nullable=False)
    questions = relationship("Question", backref="postulante",
                             cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def question(self, *args, **kwargs):
        """
        Crea objetos Questions desde el postulante
        """
        args[0]["postulante_id"] = self.id
        question = Question()
        for key, value in args[0].items():
            setattr(question, key, value)
        return question
