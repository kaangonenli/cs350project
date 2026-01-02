import os
import datetime

def scan_files(folder_path, max_files=None):
    file_data = []

    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return file_data

    print(f"Starting scan on: {folder_path}")
    if max_files:
        print(f"Note: Limited to {max_files:,} files")

    count = 0

    skip_dirs = {'.Trash', 'Library/Caches', '$RECYCLE.BIN', '.git', 'node_modules', '__pycache__'}

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not any(skip in os.path.join(root, d) for skip in skip_dirs)]
        
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
                modified_time = os.path.getmtime(file_path)
            except:
                continue

            extension = os.path.splitext(filename)[1].lower()
            modified_date = datetime.datetime.fromtimestamp(modified_time)

            file_data.append({
                "path": file_path,
                "size": size,
                "extension": extension,
                "modified_date": modified_date
            })

            count += 1
            if count % 5000 == 0:
                print(f"\rScanned {count} files...", end="", flush=True)

            if max_files and len(file_data) >= max_files:
                print(f"\n\nReached limit ({max_files:,}). Stopping.")
                return file_data

    print(f"\n\nScan complete! Found {len(file_data):,} files.")
    return file_data