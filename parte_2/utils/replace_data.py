import pandas as pd
def replace_data(csv_path, od_replacement="Seg. Odontológica", amb_replacement="Seg. Ambulatorial"):
    df = pd.read_csv(csv_path)

    replacements = {
        "OD": od_replacement,
        "AMB": amb_replacement
    }

    df = df.replace(replacements)

    df.to_csv(csv_path, index=False)
    print(f"Dados salvos com as substituições em {csv_path}")