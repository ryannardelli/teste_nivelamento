from flask import Flask, jsonify

from parte_4.server.utils.get_data_from_csv import get_data_from_csv

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Caminho para o arquivo CSV
    path = "C:/Users/Ryan/Documents/teste_tecnico/parte_4/server/Relatorio_cadop.csv"

    data = get_data_from_csv(path)

    # Retornando os dados como resposta JSON
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
