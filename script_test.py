#!/usr/bin/python3
#from models.base_model import BaseModel
from models.postulante import Postulante

name = "zoltan"
email = "zmoragarcia@gmail.com"
test = Postulante(name=name, email=email)
data_pregunta_1 = {"num_question": 3, "etapa": "1", "puntaje": "4"}
pregunta_1 = test.question(data_pregunta_1)
print("----->", test)
print(">>>>>>", pregunta_1)

