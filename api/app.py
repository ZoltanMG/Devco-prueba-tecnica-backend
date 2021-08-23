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
        lista_questios_tmp = []
        for question in postulante.questions:
            lista_questios_tmp.append(question.to_dict())
        diccionario_temp["preguntas"] = lista_questios_tmp
        postulantes_json.append(diccionario_temp)    
    new_dict = {"postulantes": postulantes_json}
    return new_dict


@app.route("/", methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
def home():
    if request.method == "GET":
        postulantes = storage.session.query(Postulante).all()
        postulantes_json = json_postulantes(postulantes)
        return postulantes_json, 200
    elif request.method == "POST":
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
            question = storage.session.query(Question).filter_by(numero_pregunta=pregunta["numero_pregunta"], etapa=pregunta["etapa"]).first()
            if question:
                for key,value in pregunta.items():
                    setattr(question, key, value)
            else:
                question = postulante.question(pregunta)
            print(question)
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
