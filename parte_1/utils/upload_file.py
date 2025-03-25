import requests
import os

def upload_file(url, name_archive):
    print(f"Baixando o arquivo {name_archive}")

    response = requests.get(url)

    if response.status_code == 200:
        print(f"Download do arquivo {name_archive} foi bem-sucedido!")
        if not os.path.exists('assets'):
            os.makedirs('assets')

        path_archive = os.path.join('assets', name_archive)

        with open(path_archive, "wb") as file:
            file.write(response.content)
    else:
        print(f"Erro ao baixar o arquivo {name_archive}. Status code: {response.status_code}")


links = [
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf',
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
]

name_archives = [
    'Anexo_I.pdf',
    'Anexo_II.pdf'
]