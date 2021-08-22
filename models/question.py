#!/usr/bin/python3
from models import postulante
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey

class Question(BaseModel, Base):

    __tablename__ = "questions"
    postulante_id = Column(String(60), ForeignKey(
        'postulantes.id'), nullable=False)
    etapa = Column(String(2), nullable=True)
    numero_pregunta = Column(Integer(), nullable=True)
    puntaje = Column(Integer(), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)