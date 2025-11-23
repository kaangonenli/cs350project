import os
import datetime

def scan_files(folder_path):
    """
    Recursively scans the folder and all subfolders.
    Returns a list of dictionaries: {"path", "size", "extension", "modified_date"}
    """
    file_data = []

    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder does not exist: {folder_path}")
        return file_data

    # Recursive scan
    for root, dirs, files in os.walk(folder_path, topdown=True, followlinks=False):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
                modified_time = os.path.getmtime(file_path)
            except Exception as e:
                # Okunamayan dosyayı atla
                print(f"[WARNING] Cannot read file: {file_path} -> {e}")
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
