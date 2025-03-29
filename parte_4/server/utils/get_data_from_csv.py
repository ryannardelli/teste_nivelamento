import pandas as pd

def get_data_from_csv(path):
    # Lendo o CSV com pandas usando o caminho fornecido
    df = pd.read_csv(path, delimiter=';')

    # Substituindo NaN por um nome padrão
    df['Razao_Social'].fillna('Nome Não Disponível', inplace=True)
    df['Nome_Fantasia'].fillna('Nome Não Disponível', inplace=True)

    # Transformando o dataframe em uma lista de dicionários
    data = df[['Razao_Social', 'Nome_Fantasia', 'CNPJ']].to_dict(orient='records')
    return data
