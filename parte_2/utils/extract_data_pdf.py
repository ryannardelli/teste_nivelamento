import sys
import time
import threading
import pdfplumber

pdf_path = "Anexo_I.pdf"
csv_path = "data_extract.csv"

def loading_spinner():
    spinner = ['|', '/', '-', '\\']
    while not loading_done[0]:  # Continua até que o flag loading_done seja True
        for symbol in spinner:
            sys.stdout.write(f'\rAguarde... Isso pode demorar um pouco {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)

def extract_data_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text()
        return all_text

def extract_pdf_data():
    global extracted_data
    extracted_data = extract_data_pdf(pdf_path)
    loading_done[0] = True  # Define o flag como True quando a extração terminar

# Flag para controlar o spinner
loading_done = [False]
extracted_data = None

spinner_thread = threading.Thread(target=loading_spinner)
spinner_thread.start()

extract_thread = threading.Thread(target=extract_pdf_data)
extract_thread.start()
