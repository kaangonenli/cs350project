import os
import datetime

def scan_files(folder_path):
    file_data = []

    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return file_data

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Permission error handling
            try:
                size = os.path.getsize(file_path)
                modified_time = os.path.getmtime(file_path)
            except Exception as e:
                print(f"Error reading file: {file_path} -> {e}")
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
