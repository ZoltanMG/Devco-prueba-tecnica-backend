#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response
from models.question import Question
from models.postulante import Postulante
from models import storage
"""
Aquí se gestionan las peticiones http.
"""


# app es la instancia de Flask
app = Flask(__name__)

# llamada de la libreria Cors
CORS(app)


def json_postulantes(postulantes):
    """
    Esta función construye un diccionario con los 
    postulantesy sus respectivos datos de preguntas.
    """
    postulantes_json = []
    for postulante in postulantes:
        diccionario_temp = postulante.to_dict()
        lista_questions_tmp = []
        for question in postulante.questions:
            lista_questions_tmp.append(question.to_dict())
        lista_questions = sorted(
            lista_questions_tmp, key=lambda numero_pregunta: numero_pregunta['numero_pregunta'])
        diccionario_temp["preguntas"] = lista_questions
        postulantes_json.append(diccionario_temp)
    new_dict = {"postulantes": postulantes_json}
    return new_dict

# Endpoints


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    Este endpoint es la raíz de la app donde se envía un
    Json con toda la información almacenada.
    """
    if request.method == "GET":
        postulantes = storage.session.query(Postulante).all()
        postulantes_json = json_postulantes(postulantes)
        return postulantes_json, 200
    return jsonify({"estado": "Error"})


@app.route("/postulantes", methods=['POST', 'DELETE'], strict_slashes=False)
def postulantes():
    """
    En este endpoint se realiza la creación y eliminación de los postulantes.
    """
    if request.method == "POST":
        name = request.json["nombre"]
        nuevo_postulante = Postulante(name=name)
        nuevo_postulante.save()
        return jsonify({"estado": "creado"}), 200
    elif request.method == "DELETE":
        postulante = storage.session.query(
            Postulante).filter_by(id=request.json).first()
        postulante.delete()
        storage.save()
    return jsonify({"estado": "Error"})


@app.route("/preguntas", methods=['POST', 'PUT'], strict_slashes=False)
def preguntas():
    """
    En este endpoint se realiza la creación y actualizacion de las preguntas.
    """
    if request.method == "POST":
        for pregunta in request.json:
            postulante = storage.session.query(Postulante).filter_by(
                id=pregunta["postulante_id"]).first()
            question = postulante.question(pregunta)
            question.save()
        return {"estado": "creado"}
    if request.method == "PUT":
        for pregunta in request.json:
            question = storage.session.query(
                Question).filter_by(id=pregunta["id"]).first()
            for key, value in pregunta.items():
                setattr(question, key, value)
            question.save()
        return {"estado": "atualizado"}
    return {"estado": "error"}


@app.after_request
def after(response):
    """
    Esta función verifica la sesión después de una solicitud y
    le da al CORS con la interfaz que permite la conexión
    entre la parte posterior y la frontal.
    """
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
