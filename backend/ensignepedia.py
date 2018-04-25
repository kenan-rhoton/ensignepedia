from cercador import cercador 
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def get_url(paraula):
    cercador.url(paraula)
