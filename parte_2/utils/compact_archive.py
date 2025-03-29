import zipfile
import os

def compact_archive(folder_path, zip_name):
    zip_path = os.path.join(folder_path, zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)

    print(f"Arquivo ZIP '{zip_name}' foi criado com sucesso!")
