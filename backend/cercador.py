import os.path
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def paraula_existeix(paraula):
    return os.path.isfile("videos/" + paraula.lower() + ".gif")

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def url(paraula):
    paraula = paraula.lower();
    if paraula_existeix(paraula):
        return "../backend/videos/" + paraula + ".gif"
    else:
        return "SenseResultat"
