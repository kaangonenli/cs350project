from scanner import scan_files
from pdf_cdf import calculate_pdf, calculate_cdf
import numpy as np

# --- Yardımcı Fonksiyonlar ---
def bytes_to_mb(x):
    return round(x / (1024*1024), 2)

def bytes_to_gb(x):
    return round(x / (1024*1024*1024), 2)

# --- Mod Seçimi ---
use_test_folder = False  # True → test klasörü, False → terminal input

if use_test_folder:
    folder = r"C:\Users\kaang\Documents"  # Test klasörü
else:
    folder = input("Enter folder path to scan: ")

# --- Tarama ---
print("Scanning...\n")
file_data = scan_files(folder)
file_sizes = [f["size"] for f in file_data]

total_files = len(file_sizes)
total_size = sum(file_sizes)

print(f"Total files: {total_files}")
print(f"Total size: {bytes_to_gb(total_size)} GB")

# --- PDF ve CDF Hesaplama ---
counts, bins = calculate_pdf(file_sizes)
sorted_sizes, cdf = calculate_cdf(file_sizes)

print("\nPDF calculated:", len(counts), "bins")
print("CDF calculated.\n")

# --- Soru 1: 90% dosya 100KB’dan küçük mü? ---
size_100kb = 100 * 1024
idx = np.searchsorted(sorted_sizes, size_100kb)
cdf_100kb = cdf[idx] if idx < len(cdf) else 1.0
answer1 = "YES" if cdf_100kb >= 0.9 else "NO"
print(f"QUESTION 1: Are 90% of files smaller than 100KB?")
print(f"CDF(100KB) = {cdf_100kb*100:.2f}% → ANSWER: {answer1}\n")

# --- Soru 2: En büyük 10% dosya disk alanının %90’ını mı kullanıyor? ---
largest_10_count = int(len(file_sizes)*0.10)
largest_sizes_sum = sum(sorted_sizes[-largest_10_count:])
answer2 = "YES" if (largest_sizes_sum / total_size) >= 0.9 else "NO"
print("QUESTION 2: Do the largest 10% of files occupy 90% of disk space?")
print(f"Largest 10% files = {bytes_to_gb(largest_sizes_sum)} GB ({largest_sizes_sum/total_size*100:.2f}%) → ANSWER: {answer2}")
