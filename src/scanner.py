import os
import datetime
import sys

def scan_files(folder_path):
    file_data = []

    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return file_data

    print(f"Starting full scan on: {folder_path}")
    print("Scanning... (This will take a while if it is C: drive)")
    
    count = 0


    for root, dirs, files in os.walk(folder_path):
        
        for filename in files:
            file_path = os.path.join(root, filename)

            try:

                size = os.path.getsize(file_path)
                modified_time = os.path.getmtime(file_path)
            except (PermissionError, OSError):

                continue
            except Exception:
                continue

            extension = os.path.splitext(filename)[1].lower()
            modified_date = datetime.datetime.fromtimestamp(modified_time)

            file_data.append({
                "path": file_path,
                "size": size,
                "extension": extension,
                "modified_date": modified_date
            })

            # Visual feedback so you know it's not frozen
            count += 1
            if count % 5000 == 0:
                print(f"\rScanned {count} files...", end="", flush=True)

    print(f"\n\nScan complete! Found {len(file_data)} accessible files.")
    return file_data