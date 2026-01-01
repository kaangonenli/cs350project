import os
import random
from datetime import datetime, timedelta

def create_test_folder(base_path="test_folder", num_files=200):
    print(f"Creating test folder: {base_path}")

    os.makedirs(base_path, exist_ok=True)

    # Subfolders
    subfolders = ["Documents", "Pictures", "Videos", "Music", "Downloads", "Projects"]

    for subfolder in subfolders:
        os.makedirs(os.path.join(base_path, subfolder), exist_ok=True)

    print(f"Created {len(subfolders)} subfolders")

    # File extensions for each folder
    extensions = {
        'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx'],
        'Pictures': ['.jpg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.flac', '.m4a'],
        'Downloads': ['.zip', '.rar', '.exe', '.iso'],
        'Projects': ['.py', '.java', '.cpp', '.html', '.css']
    }

    files_created = 0

    # Create files in each folder
    for folder_name, exts in extensions.items():
        folder_path = os.path.join(base_path, folder_name)
        files_in_folder = num_files // len(subfolders)

        for i in range(files_in_folder):
            # File size distribution: 70% small, 20% medium, 10% large
            rand = random.random()
            if rand < 0.7:
                size = random.randint(1000, 100000)  # 1KB - 100KB
            elif rand < 0.9:
                size = random.randint(100000, 5000000)  # 100KB - 5MB
            else:
                size = random.randint(5000000, 100000000)  # 5MB - 100MB

            ext = random.choice(exts)
            filename = f"file_{i:03d}{ext}"
            filepath = os.path.join(folder_path, filename)

            with open(filepath, 'wb') as f:
                f.write(b'X' * size)

            # Random modification time (last 3 years)
            days_ago = random.randint(0, 1095)
            old_time = datetime.now() - timedelta(days=days_ago)
            timestamp = old_time.timestamp()
            os.utime(filepath, (timestamp, timestamp))

            files_created += 1

    # Add some files in root folder
    for i in range(20):
        size = random.randint(1000, 50000)
        ext = random.choice(['.txt', '.log', '.ini', '.cfg'])
        filename = f"readme_{i}{ext}"
        filepath = os.path.join(base_path, filename)

        with open(filepath, 'wb') as f:
            f.write(b'X' * size)
        files_created += 1

    total_size = sum(os.path.getsize(os.path.join(root, file))
                     for root, dirs, files in os.walk(base_path)
                     for file in files)

    print(f"Created {files_created} files")
    print(f"Total size: {total_size / (1024 * 1024):.2f} MB")
    print(f"\nTest folder ready: {os.path.abspath(base_path)}")

    return os.path.abspath(base_path)

if __name__ == "__main__":
    print("=" * 60)
    print("TEST FOLDER CREATOR")
    print("=" * 60)
    print()

    print("Where to create test folder?")
    print("1. Current directory (test_folder)")
    print("2. Custom path")

    choice = input("\nChoice (1/2): ").strip()

    if choice == "2":
        custom_path = input("Enter folder path: ").strip()
    else:
        custom_path = "test_folder"

    num_files = input("\nHow many files to create? (default: 200): ").strip()
    num_files = int(num_files) if num_files else 200

    print()
    print("=" * 60)

    folder_path = create_test_folder(custom_path, num_files)

    print()
    print("=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print(f"\nYou can now test the project:")
    print(f"python main.py")
    print(f"\nFolder path: {folder_path}")