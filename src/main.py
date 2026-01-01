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

def bytes_to_mb(x):
    return round(x / (1024 * 1024), 2)

def bytes_to_gb(x):
    return round(x / (1024 * 1024 * 1024), 2)

# Print system information
print("\n" + "=" * 70)
print("FILE SYSTEM ANALYZER")
print("=" * 70)
print(f"\nSystem: {platform.system()} ({platform.platform()})")
print(f"Architecture: {platform.machine()}")
print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# Test mode or manual input
use_test_folder = False

if use_test_folder:
    folder = r"C:\Users\kaang\Documents"
else:
    folder = input("\nEnter folder path to scan (e.g., C:\\ or /Users): ").strip()

if not os.path.isdir(folder):
    print("\n[ERROR] Invalid directory path.\n")
    exit()

print(f"\n[INFO] Scanning: {folder}")
print("[WARNING] This may take several minutes for full disk scan...")
print("\nScanning...\n")

file_data = scan_files(folder)

if not file_data:
    print("No files found!")
    exit()

file_sizes = [f["size"] for f in file_data]
total_files = len(file_sizes)
total_size = sum(file_sizes)

print(f"Total files: {total_files}")
print(f"Total size: {bytes_to_gb(total_size)} GB")

# Calculate PDF and CDF
counts, bins = calculate_pdf(file_sizes)
sorted_sizes, cdf = calculate_cdf(file_sizes)

print("\nPDF calculated:", len(counts), "bins")
print("CDF calculated.\n")

# Question 1: Are 90% of files smaller than 100KB?
size_100kb = 100 * 1024
idx = np.searchsorted(sorted_sizes, size_100kb)
cdf_100kb = cdf[idx] if idx < len(cdf) else 1.0
answer1 = "YES" if cdf_100kb >= 0.9 else "NO"

print("QUESTION 1: Are 90% of files smaller than 100KB?")
print(f"CDF(100KB) = {cdf_100kb * 100:.2f}% -> ANSWER: {answer1}\n")

# Question 2: Do the largest 10% of files use 90% of disk space?
largest_10_count = int(len(file_sizes) * 0.10)
largest_sizes_sum = sum(sorted_sizes[-largest_10_count:])
percentage = (largest_sizes_sum / total_size) * 100
answer2 = "YES" if percentage >= 90 else "NO"

print("QUESTION 2: Do the largest 10% of files occupy 90% of disk space?")
print(f"Largest 10% files = {bytes_to_gb(largest_sizes_sum)} GB ({percentage:.2f}%) -> ANSWER: {answer2}")

# Detailed analysis
print("\n" + "=" * 60)
print("DETAILED ANALYSIS")
print("=" * 60)

calculate_statistics(file_sizes)
analyze_extensions(file_data, top_n=20)  # Top-20 extensions by count
analyze_by_extension_size(file_data, top_n=20)  # Top-20 extensions by size
find_large_files(file_data, threshold_mb=50)
analyze_time_distribution(file_data)

# Generate plots
print("\n" + "=" * 60)
print("GENERATING PLOTS...")
print("=" * 60)

try:
    print("\n1. Normal scale PDF and CDF...")
    plot_both(counts, bins, sorted_sizes, cdf)

    print("\n2. Logarithmic scale PDF and CDF...")
    plot_size_distribution_log(counts, bins, sorted_sizes, cdf)

    print("\nPlots generated successfully!")
except Exception as e:
    print(f"\nError: {e}")
    print("Note: Install matplotlib with 'pip install matplotlib'")

# Export results to JSON
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
print("ANALYSIS COMPLETE!")
print("=" * 60)
print(f"\nResults saved to: {output_filename}")
print("\nTo compare with another system:")
print(f"  python compare_systems.py {output_filename} <other_result.json>")
print("=" * 60)