#!/usr/bin/python3
from models.postulante import Postulante
"""
Aquí se crean postulantes y respuestas de preguntas para testeo
"""

name = "Zoltán Mora García"
postulante_zoltan = Postulante(name=name)
postulante_zoltan.save()
data_pregunta_zoltan_1 = {"numero_pregunta": 1, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_2 = {"numero_pregunta": 2, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_3 = {"numero_pregunta": 3, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_4 = {"numero_pregunta": 4, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_5 = {"numero_pregunta": 5, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_6 = {"numero_pregunta": 6, "etapa": "1", "puntaje": "-1", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_7 = {"numero_pregunta": 7, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_zoltan_8 = {"numero_pregunta": 8, "etapa": "1", "puntaje": "-1", "descripcion": "esta es una descripción temporal"}
pregunta_zoltan_1 = postulante_zoltan.question(data_pregunta_zoltan_1)
pregunta_zoltan_1.save()
pregunta_zoltan_2 = postulante_zoltan.question(data_pregunta_zoltan_2)
pregunta_zoltan_2.save()
pregunta_zoltan_3 = postulante_zoltan.question(data_pregunta_zoltan_3)
pregunta_zoltan_3.save()
pregunta_zoltan_4 = postulante_zoltan.question(data_pregunta_zoltan_4)
pregunta_zoltan_4.save()
pregunta_zoltan_5 = postulante_zoltan.question(data_pregunta_zoltan_5)
pregunta_zoltan_5.save()
pregunta_zoltan_6 = postulante_zoltan.question(data_pregunta_zoltan_6)
pregunta_zoltan_6.save()
pregunta_zoltan_7 = postulante_zoltan.question(data_pregunta_zoltan_7)
pregunta_zoltan_7.save()
pregunta_zoltan_8 = postulante_zoltan.question(data_pregunta_zoltan_8)
pregunta_zoltan_8.save()

name = "María Paula Ortiz Martínez"
postulante_maria = Postulante(name=name)
postulante_maria.save()
data_pregunta_maria_1 = {"numero_pregunta": 1, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_2 = {"numero_pregunta": 2, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_3 = {"numero_pregunta": 3, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_4 = {"numero_pregunta": 4, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_5 = {"numero_pregunta": 5, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_6 = {"numero_pregunta": 6, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_7 = {"numero_pregunta": 7, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
data_pregunta_maria_8 = {"numero_pregunta": 8, "etapa": "1", "puntaje": "4", "descripcion": "esta es una descripción temporal"}
pregunta_maria_1 = postulante_maria.question(data_pregunta_maria_1)
pregunta_maria_1.save()
pregunta_maria_2 = postulante_maria.question(data_pregunta_maria_2)
pregunta_maria_2.save()
pregunta_maria_3 = postulante_maria.question(data_pregunta_maria_3)
pregunta_maria_3.save()
pregunta_maria_4 = postulante_maria.question(data_pregunta_maria_4)
pregunta_maria_4.save()
pregunta_maria_5 = postulante_maria.question(data_pregunta_maria_5)
pregunta_maria_5.save()
pregunta_maria_6 = postulante_maria.question(data_pregunta_maria_6)
pregunta_maria_6.save()
pregunta_maria_7 = postulante_maria.question(data_pregunta_maria_7)
pregunta_maria_7.save()
pregunta_maria_8 = postulante_maria.question(data_pregunta_maria_8)
pregunta_maria_8.save()



