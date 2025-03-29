from parte_2.utils.compact_archive import compact_archive
from parte_2.utils.extract_data_pdf import extract_data_pdf
from parte_2.utils.replace_data import replace_data
from parte_2.utils.save_data_to_csv import save_data_to_csv
import os

# Caminhos dos arquivos
pdf_path = "Anexo_I.pdf"
csv_filename = "data_extract.csv"
assets_folder = "assets"
csv_path = os.path.join(assets_folder, csv_filename)

data = extract_data_pdf(pdf_path)

# Definição dos textos a serem substituídos
od = "Seg. Odontológica"
amb = "Seg. Ambulatorial"
name_zip = "Teste_Ryan.zip"

if not os.path.exists(assets_folder):
    os.makedirs(assets_folder)

save_data_to_csv(data, csv_filename)

replace_data(csv_filename, od, amb)

compact_archive(assets_folder, name_zip)

print(f"Processo concluído! CSV salvo e compactado em {name_zip}.")
