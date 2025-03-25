# Here are importing functions locais
from parte_1.utils.upload_file import upload_file
from parte_1.utils.zip_folders import zip_assets_folder

links = [
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf',
    'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
]

name_archives = [
    'Anexo_I.pdf',
    'Anexo_II.pdf'
]

for i in range(len(links)):
    upload_file(links[i], name_archives[i])

zip_assets_folder('assets', 'anexos_files.zip')