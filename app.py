from flask import Flask , render_template
from flask import jsonify
from flask import request

import json

topics = [
    {
        'id': 1,
        'title': "Titulo",
        'type':"Jusbrasil"
    },
    {
        'id': 2,
        'title': "Vaga",
        'type':"Desenvolvedor na Jusbrasil"
    },
    {
        'id': 3,
        'title': "Front End",
        'type':"CSS"
    },
    {
        'id': 4,
        'title': "BackEnd",
        'type':"Python"
    },
    {
        'id': 5,
        'title': "Data Science",
        'type':"Data Mining"
    },
    {
        'id': 6,
        'title': "Tecnologia e o futuro",
        'type':"Tecnologia"
    },
    {
        'id': 7,
        'title': "Voce ja ouviu falar da nova Tech Pix?",
        'type':"Filmadora"
    },
]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# Função que irá retornar os dados ao bater na rota
@app.route('/entities/')
def retornajson():        
    return jsonify(topics)

@app.route('/entities/post',methods=['POST'])
def postjson():
    id = len(topics) -1 
    req = {
        "id" :id,
        "title":request.get_json(force=True).get('title'),
        "type":request.get_json(force=True).get('type')

    }
    topics.append(req)
    return jsonify(topics)


@app.route('/entities/search=<letter>',methods=['GET'])
def getTopic(letter):
    response = []
    for topic in topics:
        if topic['type'].startswith(letter, 0 , len(topic['type'])) is True:
            response.append(topic)
    
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=False)


