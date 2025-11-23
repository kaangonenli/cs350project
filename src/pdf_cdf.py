import numpy as np

def calculate_pdf(file_sizes, bins=50):
    """
    PDF (Histogram) hesaplar.
    """
    counts, bin_edges = np.histogram(file_sizes, bins=bins)
    return counts, bin_edges


def calculate_cdf(file_sizes):
    """
    CDF hesaplar (kümülatif dağılım).
    """
    sizes = np.array(file_sizes)
    sizes_sorted = np.sort(sizes)
    cdf_values = np.arange(1, len(sizes_sorted) + 1) / len(sizes_sorted)
    return sizes_sorted, cdf_values
