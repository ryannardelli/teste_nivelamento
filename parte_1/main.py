# Here are importing functions locais
from parte_1.utils.findArchive import findArchive
from parte_1.utils.upload_file import upload_file

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
link = findArchive(url)

if link:
    name_archive = link.split('/')[-1]
    upload_file(link, name_archive)
else:
    print("None archive found to download")