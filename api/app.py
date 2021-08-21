#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import postulante
from models.postulante import Postulante
from models import storage


app = Flask(__name__)
CORS(app)


def json_postulantes(postulantes):
    postulantes_json = []
    for postulante in postulantes:
        postulantes_json.append(postulante.to_dict())
    new_dict = {"a": postulantes_json}
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
        print(request.json)
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
