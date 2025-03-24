import zipfile
import os

def zip_assets_folder(folder_path, zip_name):
    zip_path = os.path.join(folder_path, zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

    print(f"Archive ZIP went created {zip_name} with success !")