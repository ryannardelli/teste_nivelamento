from flask import Flask, jsonify

app = Flask(__name__)

data = {
    'id': '1',
    'nome': '<NAME>',
    'email': '<EMAIL>',
}

@app.route('/api', methods=['GET'])
def get_data():
    data = {"message": "Esta é uma resposta da API!"}
    return jsonify(data)

app.run(port=5000, host='localhost', debug=True)