from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from gpt import aiProcess
import json
import re


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/ai", methods=["POST"])
def ai():
    body = request.get_json()
    result = aiProcess(body["token"], body["msg"])

    return result

@app.route("/quiz", methods=["POST"])
@cross_origin()
def quiz():
    regex = r'[\\.\n]'
    body = request.get_json()
    request_template_gpt = "Crie para mim um json. Este json deve conter uma pergunta, cinco opções, sendo uma verdadeira e as demais falsas, a última chave do json, deve conter a resposta correta. O tema abordado será {}. Essa estrutura de opções, deverá ser de A até E. Para cada opções, a sua chave deve ser apena 'A', 'B', 'C', 'D' e 'E'. Por fim, transforme tudo isso em uma string sem quebras de linhas e sem caractéres especiais. GPT, essa última etapa é a que você deve me devolver em português do Brasil".format(body["msg"])
    response = json.loads(str(re.sub(regex, "", aiProcess(body["token"], request_template_gpt)['response_gpt'])))
    return jsonify(response)

app.run()