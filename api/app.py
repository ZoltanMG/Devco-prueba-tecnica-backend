#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response
from models.question import Question
from models.postulante import Postulante
from models import storage


app = Flask(__name__)
CORS(app)


def json_postulantes(postulantes):
    postulantes_json = []
    for postulante in postulantes:
        diccionario_temp = postulante.to_dict()
        lista_questions_tmp = []
        for question in postulante.questions:
            lista_questions_tmp.append(question.to_dict())
        lista_questions = sorted(lista_questions_tmp, key=lambda numero_pregunta : numero_pregunta['numero_pregunta'])
        diccionario_temp["preguntas"] = lista_questions
        postulantes_json.append(diccionario_temp)
    new_dict = {"postulantes": postulantes_json}
    return new_dict


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    if request.method == "GET":
        postulantes = storage.session.query(Postulante).all()
        postulantes_json = json_postulantes(postulantes)
        return postulantes_json, 200
    return jsonify({"estado": "Error"})

@app.route("/postulantes", methods=['POST', 'DELETE'], strict_slashes=False)
def postulantes():
    if request.method == "POST":
        name = request.json["nombre"]
        nuevo_postulante = Postulante(name=name)
        nuevo_postulante.save()
        return jsonify({"estado": "creado"}), 200
    elif request.method == "DELETE":
        postulante = storage.session.query(Postulante).filter_by(id=request.json).first()
        postulante.delete()
        storage.save()
    return jsonify({"estado": "Error"})

@app.route("/preguntas", methods=['POST', 'DELETE'], strict_slashes=False)
def preguntas():
    if request.method == "POST":
        for pregunta in request.json:
            postulante = storage.session.query(Postulante).filter_by(id=pregunta["postulante_id"]).first()
            question = postulante.question(pregunta)
            print(question.to_dict())
            question.save()

        return {"estado": "creado"}
    return {"estado": "error"}



@app.after_request
def after(response):
    # This function verifies the session after a request
    # and gives the CORS with the frontend
    # allows the conncetion between the back and the front
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
