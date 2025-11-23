from scanner import scan_files
from pdf_cdf import calculate_pdf, calculate_cdf
from plotter import plot_both, plot_size_distribution_log
from analyze import (analyze_extensions, analyze_by_extension_size,
                     calculate_statistics, find_large_files, analyze_time_distribution)
import numpy as np
import os


# --- Helper Functions ---
def bytes_to_mb(x):
    return round(x / (1024 * 1024), 2)


def bytes_to_gb(x):
    return round(x / (1024 * 1024 * 1024), 2)


# --- Input Mode ---
use_test_folder = False  # True → test folder, False → manual input

if use_test_folder:
    folder = r"C:\Users\kaang\Documents"
else:
    folder = input("Enter folder path to scan: ").strip()

# --- Path Validation ---
if not os.path.isdir(folder):
    print("\n[ERROR] Invalid directory path. Calculation aborted.\n")
    exit()

print(f"\n[INFO] Scanning directory: {folder}\n")

# --- Scan ---
print("Scanning...\n")
file_data = scan_files(folder)

if not file_data:
    print("Hiç dosya bulunamadı veya klasör okunamadı!")
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
analyze_extensions(file_data)
analyze_by_extension_size(file_data)
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

print("\n" + "=" * 60)
print("ANALİZ TAMAMLANDI!")
print("=" * 60)
