import numpy as np
from collections import Counter


def analyze_extensions(file_data):
    """Dosya uzantılarına göre analiz yapar"""
    extensions = [f["extension"] for f in file_data if f["extension"]]
    ext_counter = Counter(extensions)

    print("\n=== DOSYA UZANTILARINA GÖRE ANALİZ ===")
    print(f"Toplam farklı uzantı: {len(ext_counter)}")
    print("\nEn yaygın 10 uzantı:")
    for ext, count in ext_counter.most_common(10):
        print(f"  {ext:15} : {count:6} dosya")

    return ext_counter


def analyze_by_extension_size(file_data):
    """Her uzantı için toplam disk kullanımı"""
    ext_sizes = {}
    for f in file_data:
        ext = f["extension"] if f["extension"] else "uzantısız"
        if ext not in ext_sizes:
            ext_sizes[ext] = []
        ext_sizes[ext].append(f["size"])

    # Toplam boyuta göre sırala
    ext_total = [(ext, sum(sizes)) for ext, sizes in ext_sizes.items()]
    ext_total.sort(key=lambda x: x[1], reverse=True)

    print("\n=== UZANTILARA GÖRE DİSK KULLANIMI (İLK 10) ===")
    for ext, total in ext_total[:10]:
        print(f"  {ext:15} : {total / (1024 * 1024 * 1024):.2f} GB")

    return ext_total


def analyze_time_distribution(file_data):
    """Dosyaların zamansal dağılımı"""
    dates = [f["modified_date"] for f in file_data]
    years = [d.year for d in dates]
    year_counter = Counter(years)

    print("\n=== YILLARA GÖRE DOSYA DAĞILIMI ===")
    for year in sorted(year_counter.keys()):
        print(f"  {year}: {year_counter[year]:6} dosya")

    return year_counter


def calculate_statistics(file_sizes):
    """Temel istatistikleri hesaplar"""
    sizes = np.array(file_sizes)

    print("\n=== İSTATİSTİKSEL ÖZETİ ===")
    print(f"Ortalama boyut: {np.mean(sizes) / (1024):.2f} KB")
    print(f"Medyan boyut:   {np.median(sizes) / (1024):.2f} KB")
    print(f"Standart sapma: {np.std(sizes) / (1024):.2f} KB")
    print(f"Min boyut:      {np.min(sizes)} bytes")
    print(f"Max boyut:      {np.max(sizes) / (1024 * 1024):.2f} MB")
    print(f"\nYüzdelik Dilimler (Percentiles):")
    print(f"  25%: {np.percentile(sizes, 25) / (1024):.2f} KB")
    print(f"  50%: {np.percentile(sizes, 50) / (1024):.2f} KB")
    print(f"  75%: {np.percentile(sizes, 75) / (1024):.2f} KB")
    print(f"  90%: {np.percentile(sizes, 90) / (1024):.2f} KB")
    print(f"  95%: {np.percentile(sizes, 95) / (1024 * 1024):.2f} MB")
    print(f"  99%: {np.percentile(sizes, 99) / (1024 * 1024):.2f} MB")


def find_large_files(file_data, threshold_mb=100):
    """Belirli boyuttan büyük dosyaları bulur"""
    threshold_bytes = threshold_mb * 1024 * 1024
    large_files = [f for f in file_data if f["size"] > threshold_bytes]
    large_files.sort(key=lambda x: x["size"], reverse=True)

    print(f"\n=== {threshold_mb}MB'DAN BÜYÜK DOSYALAR (İLK 20) ===")
    for i, f in enumerate(large_files[:20], 1):
        size_mb = f["size"] / (1024 * 1024)
        print(f"{i:2}. {size_mb:8.2f} MB - {f['path']}")

    return large_files