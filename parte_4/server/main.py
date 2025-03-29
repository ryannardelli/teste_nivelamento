from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)

df = pd.read_csv("C:/Users/Ryan/Documents/teste_tecnico/parte_4/server/Relatorio_cadop.csv", delimiter=';')

# Função para transformar o dataframe em lista de dicionários
def get_data_from_csv():
    # Filtrando as colunas mais importantes
    data = df[['Razao_Social', 'Nome_Fantasia', 'CNPJ', 'Modalidade']].to_dict(orient='records')

    # Substitui o valor vazio da coluna (NaN) por um nome mais legível
    df['Nome_Fantasia'].fillna('Nome Não Disponível', inplace=True)
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = get_data_from_csv()
    return jsonify(data)

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
