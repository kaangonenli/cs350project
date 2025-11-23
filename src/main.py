from scanner import scan_files
from pdf_cdf import calculate_pdf, calculate_cdf
import numpy as np
import os

# --- Helper Functions ---
def bytes_to_gb(x):
    return round(x / (1024*1024*1024), 2)

def normalize_path(path):
    return path.strip().strip('"').strip("'").replace("/", "\\")

# --- Input ---
use_test_folder = False

if use_test_folder:
    folder = r"C:\Users\kaang\Documents"
else:
    folder = input("Enter folder path to scan: ")

folder = normalize_path(folder)

if not os.path.isdir(folder):
    print(f"\n[ERROR] Invalid directory path. Calculation aborted.\nPATH: {folder}")
    exit()

print(f"\n[INFO] Scanning directory: {folder}\n")

# --- Scan (recursive) ---
file_data = scan_files(folder)

if not file_data:
    print(f"\n[INFO] No readable files found in directory: {folder}")
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

# --- Question 1 ---
size_100kb = 100 * 1024
idx = np.searchsorted(sorted_sizes, size_100kb)
cdf_100kb = cdf[idx] if idx < len(cdf) else 1.0
answer1 = "YES" if cdf_100kb >= 0.9 else "NO"

print("QUESTION 1: Are 90% of files smaller than 100KB?")
print(f"CDF(100KB) = {cdf_100kb*100:.2f}% → ANSWER: {answer1}\n")

# --- Question 2 ---
largest_10_count = max(1, int(len(file_sizes) * 0.10))
largest_sizes_sum = sum(sorted_sizes[-largest_10_count:])
percentage = (largest_sizes_sum / total_size) * 100
answer2 = "YES" if percentage >= 90 else "NO"

print("QUESTION 2: Do the largest 10% of files occupy 90% of disk space?")
print(f"Largest 10% files = {bytes_to_gb(largest_sizes_sum)} GB ({percentage:.2f}%) → ANSWER: {answer2}\n")
