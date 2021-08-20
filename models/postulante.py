#!/usr/bin/python3
from models.base_model import BaseModel
from models.question import Question

class Postulante(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def question(self, *args, **kwargs):
        question =  Question()
        args[0]["postulante_id"] = self.id
        for key, value in args[0].items():
            setattr(question, key, value)
        return question