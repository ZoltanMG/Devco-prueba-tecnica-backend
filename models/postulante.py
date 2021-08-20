#!/usr/bin/python3
from os import name
from models.base_model import BaseModel

class Postulante(BaseModel):
    def __init__(self, name):
        self.name = name
        super().__init__()