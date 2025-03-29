import os
import pandas as pd

def replace_data(csv_path, od_replacement="Seg. Odontológica", amb_replacement="Seg. Ambulatorial"):
    assets_folder = "assets"
    csv_full_path = os.path.join(assets_folder, csv_path)

    # Verificar se o arquivo existe no diretório correto
    if not os.path.exists(csv_full_path):
        raise FileNotFoundError(f"O arquivo {csv_full_path} não foi encontrado!")

    # Ler o CSV
    df = pd.read_csv(csv_full_path)

    replacements = {
        "OD": od_replacement,
        "AMB": amb_replacement
    }
    df = df.replace(replacements)

    df.to_csv(csv_full_path, index=False, encoding="utf-8")
    print(f"Dados salvos com as substituições em {csv_full_path}")
