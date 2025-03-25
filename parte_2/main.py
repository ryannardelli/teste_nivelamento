from parte_2.utils.compact_archive import compact_archive
from parte_2.utils.extract_data_pdf import extract_data_pdf
from parte_2.utils.replace_data import replace_data
from parte_2.utils.save_data_to_csv import save_data_to_csv

pdf_path = "Anexo_I.pdf"
csv_path = "data_extract.csv"

data = extract_data_pdf(pdf_path)

od = "Seg. Odontológica"
amb = "Seg. Ambulatorial"
name_zip = "Teste_Ryan.zip"

save_data_to_csv(data, csv_path)
compact_archive('assets', name_zip)
replace_data(csv_path, od, amb)