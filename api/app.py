#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
#from models.base_model import BaseModel
#from models.postulante import Postulante


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    #test = Postulante("Zoltan")
    #print(test)
    return {"estado": "OK"}


@app.after_request
def after(response):
    # This function verifies the session after a request
    # and gives the CORS with the frontend
    # allows the conncetion between the back and the front
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)