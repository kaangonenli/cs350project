import numpy as np
from collections import Counter

def analyze_extensions(file_data, top_n=20):
    extensions = [f["extension"] for f in file_data if f["extension"]]
    no_ext_count = sum(1 for f in file_data if not f["extension"])

    ext_counter = Counter(extensions)

    print(f"\n=== FILE EXTENSIONS ANALYSIS (TOP-{top_n}) ===")
    print(f"Total unique extensions: {len(ext_counter)}")
    print(f"Files without extension: {no_ext_count}")
    print(f"\nTop {top_n} extensions by file count:")
    for i, (ext, count) in enumerate(ext_counter.most_common(top_n), 1):
        percentage = (count / len(file_data)) * 100
        print(f"  {i:2}. {ext:15} : {count:8} files ({percentage:5.2f}%)")

    return ext_counter

def analyze_by_extension_size(file_data, top_n=20):
    ext_sizes = {}
    for f in file_data:
        ext = f["extension"] if f["extension"] else "no_ext"
        if ext not in ext_sizes:
            ext_sizes[ext] = []
        ext_sizes[ext].append(f["size"])

    ext_total = [(ext, sum(sizes), len(sizes)) for ext, sizes in ext_sizes.items()]
    ext_total.sort(key=lambda x: x[1], reverse=True)

    total_size = sum(f["size"] for f in file_data)

    print(f"\n=== DISK USAGE BY EXTENSION (TOP-{top_n}) ===")
    for i, (ext, total, count) in enumerate(ext_total[:top_n], 1):
        percentage = (total / total_size) * 100
        avg_size = total / count
        print(f"  {i:2}. {ext:15} : {total / (1024 * 1024 * 1024):8.2f} GB ({percentage:5.2f}%) | {count:8} files | Avg: {avg_size / 1024:8.2f} KB")

    return ext_total

def analyze_time_distribution(file_data):
    dates = [f["modified_date"] for f in file_data]
    years = [d.year for d in dates]
    year_counter = Counter(years)

    print("\n=== FILE DISTRIBUTION BY YEAR ===")
    for year in sorted(year_counter.keys()):
        print(f"  {year}: {year_counter[year]:6} files")

    return year_counter

def calculate_statistics(file_sizes):
    sizes = np.array(file_sizes)

    print("\n=== STATISTICAL SUMMARY ===")
    print(f"Mean:   {np.mean(sizes) / 1024:.2f} KB")
    print(f"Median: {np.median(sizes) / 1024:.2f} KB")
    print(f"Std:    {np.std(sizes) / 1024:.2f} KB")
    print(f"Min:    {np.min(sizes)} bytes")
    print(f"Max:    {np.max(sizes) / (1024 * 1024):.2f} MB")
    print(f"\nPercentiles:")
    print(f"  25%: {np.percentile(sizes, 25) / 1024:.2f} KB")
    print(f"  50%: {np.percentile(sizes, 50) / 1024:.2f} KB")
    print(f"  75%: {np.percentile(sizes, 75) / 1024:.2f} KB")
    print(f"  90%: {np.percentile(sizes, 90) / 1024:.2f} KB")
    print(f"  95%: {np.percentile(sizes, 95) / (1024 * 1024):.2f} MB")
    print(f"  99%: {np.percentile(sizes, 99) / (1024 * 1024):.2f} MB")

def find_large_files(file_data, threshold_mb=100):
    threshold_bytes = threshold_mb * 1024 * 1024
    large_files = [f for f in file_data if f["size"] > threshold_bytes]
    large_files.sort(key=lambda x: x["size"], reverse=True)

    print(f"\n=== FILES LARGER THAN {threshold_mb}MB (TOP 20) ===")
    for i, f in enumerate(large_files[:20], 1):
        size_mb = f["size"] / (1024 * 1024)
        print(f"{i:2}. {size_mb:8.2f} MB - {f['path']}")

    return large_files