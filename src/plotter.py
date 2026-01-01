import matplotlib.pyplot as plt
import numpy as np

def plot_pdf(counts, bins):
    plt.figure(figsize=(10, 6))
    plt.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    plt.xlabel('File Size (bytes)', fontsize=12)
    plt.ylabel('Number of Files', fontsize=12)
    plt.title('PDF - File Size Distribution', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_cdf(sorted_sizes, cdf):
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    plt.xlabel('File Size (bytes)', fontsize=12)
    plt.ylabel('Cumulative Probability', fontsize=12)
    plt.title('CDF - Cumulative Distribution', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0.9, color='green', linestyle='--', label='90% threshold')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_both(counts, bins, sorted_sizes, cdf):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # PDF
    ax1.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    ax1.set_xlabel('File Size (bytes)', fontsize=11)
    ax1.set_ylabel('Number of Files', fontsize=11)
    ax1.set_title('PDF - Histogram', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # CDF
    ax2.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    ax2.set_xlabel('File Size (bytes)', fontsize=11)
    ax2.set_ylabel('Cumulative Probability', fontsize=11)
    ax2.set_title('CDF - Cumulative Distribution', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0.9, color='green', linestyle='--', linewidth=1.5, label='90% threshold')
    ax2.legend()

    plt.tight_layout()
    plt.show()

def plot_size_distribution_log(counts, bins, sorted_sizes, cdf):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # PDF - Log scale
    ax1.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    ax1.set_xlabel('File Size (bytes)', fontsize=11)
    ax1.set_ylabel('Number of Files', fontsize=11)
    ax1.set_title('PDF - Logarithmic Scale', fontsize=13, fontweight='bold')
    ax1.set_xscale('log')
    ax1.grid(True, alpha=0.3, which='both')

    # CDF - Log scale
    ax2.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    ax2.set_xlabel('File Size (bytes)', fontsize=11)
    ax2.set_ylabel('Cumulative Probability', fontsize=11)
    ax2.set_title('CDF - Logarithmic Scale', fontsize=13, fontweight='bold')
    ax2.set_xscale('log')
    ax2.grid(True, alpha=0.3, which='both')
    ax2.axhline(y=0.9, color='green', linestyle='--', linewidth=1.5, label='90% threshold')
    ax2.legend()

    plt.tight_layout()
    plt.show()