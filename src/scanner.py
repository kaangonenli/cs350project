import os
import datetime

def scan_files(folder_path):
    file_data = []

    for root, _, files in os.walk(folder_path, followlinks=False):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
                modified_time = os.path.getmtime(file_path)
            except Exception:
                # Okunamayan dosyayı atla
                continue

            extension = os.path.splitext(filename)[1].lower()
            modified_date = datetime.datetime.fromtimestamp(modified_time)

            file_data.append({
                "path": file_path,
                "size": size,
                "extension": extension,
                "modified_date": modified_date
            })

    return file_data
