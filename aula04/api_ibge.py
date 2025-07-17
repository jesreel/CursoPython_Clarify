# api IBGE com flask

# importar bibliotecas do flask e requests
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/api/v1/consulta_ibge/<string:nome>", methods=['GET'])
#@app.route("/consultar_ibge/<nome>", methods=['GET'])

def consultar_ibge(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}"
    response = requests.get(url)
    return jsonify(response.json())
    


# Iniciar Servidor
if __name__ == '__main__':
    app.run(debug = True)