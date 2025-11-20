import zipfile
import os

folder = input("Enter folder name: ")
zip_name = folder + ".zip"

with zipfile.ZipFile(zip_name, "w") as z:
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            z.write(full_path)

print("Folder successfully zipped:", zip_name)
