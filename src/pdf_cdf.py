import numpy as np

def calculate_pdf(file_sizes, bins=50):
    counts, bin_edges = np.histogram(file_sizes, bins=bins)
    return counts, bin_edges

def calculate_cdf(file_sizes):
    arr = np.sort(np.array(file_sizes))
    cdf = np.arange(1, len(arr) + 1) / len(arr)
    return arr, cdf
