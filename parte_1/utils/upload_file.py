import requests
import os

def upload_file(url, name_archive):
    print(f"Tentando baixar o arquivo: {url}")
    response = requests.get(url)

    if(response.status_code == 200):
        if not os.path.exists('assets'):
            os.makedirs('assets')

        path_archive = os.path.join('assets', name_archive)

        with open(path_archive, "wb") as file:
            file.write(response.content)
        print("Archive went saved with success!")
    else:
        print(f"Throw errror {name_archive}. Status code: {response.status_code}")

links = [
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf',
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx',
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
]

name_archives = [
    'Anexo_I.pdf',
    'Anexo_I.xlsx',
    'Anexo_II.pdf'
]

for i in range(len(links)):
    upload_file(links[i], name_archives[i])

# for link, name in zip(links, name_archives):
    # upload_file(link, name)