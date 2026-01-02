import os
import datetime
import sys

def scan_files(folder_path, max_files=None):
    """
    Scan files in folder_path
    max_files: Optional limit to prevent memory issues (default: unlimited)
    """
    file_data = []

    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return file_data

    print(f"Starting full scan on: {folder_path}")
    print("Scanning... (This will take a while if it is C: drive)")
    if max_files:
        print(f"Note: Limited to {max_files:,} files to prevent memory issues")

    count = 0

    # Skip these system directories to avoid permission issues and speed up
    skip_dirs = {
        '.Trash', 'Library/Caches', 'Library/Logs',
        '$RECYCLE.BIN', 'System Volume Information',
        '.git', 'node_modules', '__pycache__',
        'Application Support/Google/Chrome/Default/Cache'
    }

    for root, dirs, files in os.walk(folder_path):
        # Skip certain directories
        dirs[:] = [d for d in dirs if not any(skip in os.path.join(root, d) for skip in skip_dirs)]
        
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
                print(f"\rScanned {count} files... (stored: {len(file_data)})", end="", flush=True)

            # Stop if max_files limit reached
            if max_files and len(file_data) >= max_files:
                print(f"\n\n[INFO] Reached maximum file limit ({max_files:,}). Stopping scan.")
                print(f"[INFO] Found {len(file_data):,} accessible files.")
                return file_data

    print(f"\n\nScan complete! Found {len(file_data):,} accessible files.")
    return file_data