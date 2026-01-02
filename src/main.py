from scanner import scan_files
from pdf_cdf import calculate_pdf, calculate_cdf
from plotter import plot_both, plot_size_distribution_log
from analyze import (analyze_extensions, analyze_by_extension_size,
                     calculate_statistics, find_large_files, analyze_time_distribution)
from export_results import export_to_json, create_summary_report
import numpy as np
import os
import platform
import datetime


# --- Helper Functions ---
def bytes_to_mb(x):
    return round(x / (1024 * 1024), 2)


def bytes_to_gb(x):
    return round(x / (1024 * 1024 * 1024), 2)


# --- System Information ---
print("\n" + "=" * 70)
print("FILE SYSTEM ANALYZER - CS350 PROJECT")
print("=" * 70)
print(f"\nSystem: {platform.system()} ({platform.platform()})")
print(f"Architecture: {platform.machine()}")
print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# --- Input Mode ---
print("\nScan Options:")
print("  1. Quick scan - Enter a specific folder path")
print("  2. Full disk scan - Scan entire system (recommended for project)")
print("  3. Exit")

choice = input("\nSelect option (1/2/3): ").strip()

if choice == "1":
    folder = input("\nEnter folder path to scan: ").strip()
elif choice == "2":
    # Detect OS and set full disk path
    current_os = platform.system()
    if current_os == "Windows":
        folder = "C:\\"
        print(f"\n[INFO] Full disk scan selected: {folder}")
        confirm = input("This will scan entire C:\\ drive. Continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Scan cancelled.")
            exit()
    elif current_os == "Darwin":  # macOS
        folder = "/Users"
        print(f"\n[INFO] Full disk scan selected: {folder}")
        confirm = input("This will scan entire /Users directory. Continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Scan cancelled.")
            exit()
    elif current_os == "Linux":
        folder = "/home"
        print(f"\n[INFO] Full disk scan selected: {folder}")
        confirm = input("This will scan entire /home directory. Continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Scan cancelled.")
            exit()
    else:
        print(f"[ERROR] Unsupported OS: {current_os}")
        exit()
elif choice == "3":
    print("Goodbye!")
    exit()
else:
    print("[ERROR] Invalid option.")
    exit()

# --- Path Validation ---
if not os.path.isdir(folder):
    print("\n[ERROR] Invalid directory path. Calculation aborted.\n")
    exit()

print(f"\n[INFO] Scanning directory: {folder}")
print("[WARNING] Full disk scan may take 10-30 minutes...\n")

# --- Scan ---
print("Scanning...\n")
file_data = scan_files(folder)

if not file_data:
    print("No files were found or folders could not be read.!")
    exit()

file_sizes = [f["size"] for f in file_data]

total_files = len(file_sizes)
total_size = sum(file_sizes)

print(f"Total files: {total_files}")
print(f"Total size: {bytes_to_gb(total_size)} GB")

# --- PDF & CDF ---
counts, bins = calculate_pdf(file_sizes)
sorted_sizes, cdf = calculate_cdf(file_sizes)

print("\nPDF calculated:", len(counts), "bins")
print("CDF calculated.\n")

# --- Question 1: Are 90% of files smaller than 100KB? ---
size_100kb = 100 * 1024
idx = np.searchsorted(sorted_sizes, size_100kb)
cdf_100kb = cdf[idx] if idx < len(cdf) else 1.0

answer1 = "YES" if cdf_100kb >= 0.9 else "NO"

print("QUESTION 1: Are 90% of files smaller than 100KB?")
print(f"CDF(100KB) = {cdf_100kb * 100:.2f}% → ANSWER: {answer1}\n")

# --- Question 2: Do the largest 10% of files use 90% of disk space? ---
largest_10_count = int(len(file_sizes) * 0.10)
largest_sizes_sum = sum(sorted_sizes[-largest_10_count:])

percentage = (largest_sizes_sum / total_size) * 100
answer2 = "YES" if percentage >= 90 else "NO"

print("QUESTION 2: Do the largest 10% of files occupy 90% of disk space?")
print(f"Largest 10% files = {bytes_to_gb(largest_sizes_sum)} GB ({percentage:.2f}%) → ANSWER: {answer2}")

# --- Detaylı Analizler ---
print("\n" + "=" * 60)
print("DETAYLI ANALİZLER")
print("=" * 60)

calculate_statistics(file_sizes)
analyze_extensions(file_data, top_n=20)  # TOP-20 by count
analyze_by_extension_size(file_data, top_n=20)  # TOP-20 by size
find_large_files(file_data, threshold_mb=50)
analyze_time_distribution(file_data)

# --- Grafikleri Göster ---
print("\n" + "=" * 60)
print("GRAFİKLER OLUŞTURULUYOR...")
print("=" * 60)

try:
    print("\n1. Normal ölçekte PDF ve CDF grafikleri gösteriliyor...")
    plot_both(counts, bins, sorted_sizes, cdf)

    print("\n2. Logaritmik ölçekte PDF ve CDF grafikleri gösteriliyor...")
    plot_size_distribution_log(counts, bins, sorted_sizes, cdf)

    print("\n✓ Tüm grafikler başarıyla oluşturuldu!")
except Exception as e:
    print(f"\n✗ Grafik oluşturulurken hata: {e}")
    print("Not: Matplotlib yüklü değilse 'pip install matplotlib' ile yükleyebilirsiniz.")

# --- Export Results to JSON ---
print("\n" + "=" * 60)
print("EXPORTING RESULTS TO JSON...")
print("=" * 60)

# Generate filename based on system and timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
system_name = platform.system().lower()
output_filename = f"scan_results_{system_name}_{timestamp}.json"

export_data = export_to_json(file_data, output_filename)

if export_data:
    create_summary_report(export_data)

print("\n" + "=" * 60)
print("ANALİZ TAMAMLANDI!")
print("=" * 60)
print(f"\nResults saved to: {output_filename}")
print("\nTo compare with another system:")
print(f"  python compare_systems.py {output_filename} <other_result.json>")
print("=" * 60)
