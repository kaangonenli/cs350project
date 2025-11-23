import matplotlib.pyplot as plt
import numpy as np


def plot_pdf(counts, bins):
    """PDF grafiğini çizer (Histogram)"""
    plt.figure(figsize=(10, 6))
    plt.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    plt.xlabel('Dosya Boyutu (bytes)', fontsize=12)
    plt.ylabel('Dosya Sayısı', fontsize=12)
    plt.title('PDF - Dosya Boyutu Dağılımı (Histogram)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_cdf(sorted_sizes, cdf):
    """CDF grafiğini çizer"""
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    plt.xlabel('Dosya Boyutu (bytes)', fontsize=12)
    plt.ylabel('Kümülatif Olasılık', fontsize=12)
    plt.title('CDF - Kümülatif Dağılım Fonksiyonu', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0.9, color='green', linestyle='--', label='90% eşiği')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_both(counts, bins, sorted_sizes, cdf):
    """Her iki grafiği yan yana gösterir"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # PDF (Sol)
    ax1.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    ax1.set_xlabel('Dosya Boyutu (bytes)', fontsize=11)
    ax1.set_ylabel('Dosya Sayısı', fontsize=11)
    ax1.set_title('PDF - Histogram', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # CDF (Sağ)
    ax2.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    ax2.set_xlabel('Dosya Boyutu (bytes)', fontsize=11)
    ax2.set_ylabel('Kümülatif Olasılık', fontsize=11)
    ax2.set_title('CDF - Kümülatif Dağılım', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0.9, color='green', linestyle='--', linewidth=1.5, label='90% eşiği')
    ax2.legend()

    plt.tight_layout()
    plt.show()


def plot_size_distribution_log(counts, bins, sorted_sizes, cdf):
    """Logaritmik ölçekte daha detaylı görünüm"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # PDF - Log Scale
    ax1.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', alpha=0.7, color='steelblue')
    ax1.set_xlabel('Dosya Boyutu (bytes)', fontsize=11)
    ax1.set_ylabel('Dosya Sayısı', fontsize=11)
    ax1.set_title('PDF - Logaritmik Ölçek', fontsize=13, fontweight='bold')
    ax1.set_xscale('log')
    ax1.grid(True, alpha=0.3, which='both')

    # CDF - Log Scale
    ax2.plot(sorted_sizes, cdf, linewidth=2, color='darkred')
    ax2.set_xlabel('Dosya Boyutu (bytes)', fontsize=11)
    ax2.set_ylabel('Kümülatif Olasılık', fontsize=11)
    ax2.set_title('CDF - Logaritmik Ölçek', fontsize=13, fontweight='bold')
    ax2.set_xscale('log')
    ax2.grid(True, alpha=0.3, which='both')
    ax2.axhline(y=0.9, color='green', linestyle='--', linewidth=1.5, label='90% eşiği')
    ax2.legend()

    plt.tight_layout()
    plt.show()