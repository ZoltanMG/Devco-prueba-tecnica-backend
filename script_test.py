#!/usr/bin/python3
#from models.base_model import BaseModel
from models.postulante import Postulante

name = "zoltan Mora García"
test = Postulante(name=name)
test.save()
data_pregunta_1 = {"numero_pregunta": 3, "etapa": "1", "puntaje": "4"}
pregunta_1 = test.question(data_pregunta_1)
pregunta_1.save()
print("----->", test)
print(">>>>>>", pregunta_1)

