import os
import pandas as pd


def save_data_to_csv(data, csv_path):
    lines = data.split("\n")

    lines = [line.strip() for line in lines if line.strip()]

    rows = [line.split("\t") for line in lines]

    headers = rows[0]

    df = pd.DataFrame(rows[1:], columns=headers)

    df.columns = df.columns.str.strip()

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    assets_folder = 'assets'
    if not os.path.exists(assets_folder):
        os.makedirs(assets_folder)

    csv_path = os.path.join(assets_folder, csv_path)

    df.to_csv(csv_path, index=False)
    print(f'Dados salvos em {csv_path}')

