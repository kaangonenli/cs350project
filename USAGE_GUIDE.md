# CS350 Project - Usage Guide

## Hocanızın Feedback'ine Göre Yapılması Gerekenler

### 1. Tam Disk Analizi (C:\ veya tüm disk)

Windows'ta:
```bash
cd src
python main.py
# Input: C:\
```

macOS'ta:
```bash
cd src
python main.py
# Input: /Users
```

**Önemli**: Küçük bir subdirectory değil, tam disk veya ana kullanıcı klasörü taraması yapmalısınız.

### 2. Top-20 File Extension Raporlama

Program otomatik olarak Top-20 raporunu hem dosya sayısına hem de disk kullanımına göre gösterir:

```
=== FILE EXTENSIONS ANALYSIS (TOP-20) ===
Top 20 extensions by file count:
   1. .txt            :    12345 files ( 15.23%)
   2. .jpg            :     9876 files ( 12.18%)
   ...

=== DISK USAGE BY EXTENSION (TOP-20) ===
   1. .mp4            :    45.23 GB (23.45%)
   2. .zip            :    32.10 GB (16.65%)
   ...
```

### 3. İki Farklı Sistem/Kullanıcı Karşılaştırması

#### Seçenek A: İki Farklı Laptop (Önerilen)

1. **Kendi laptop'unuzda** (örn: Windows):
   ```bash
   python main.py
   # C:\ girin
   # Dosya: scan_results_windows_20260101_120000.json
   ```

2. **Arkadaşınızın laptop'unda** (örn: macOS - Mimarlık, EE, Endüstri):
   ```bash
   python main.py
   # /Users girin
   # Dosya: scan_results_darwin_20260101_130000.json
   ```

3. **JSON dosyalarını birleştirip karşılaştırın**:
   ```bash
   python compare_systems.py scan_results_windows_20260101_120000.json scan_results_darwin_20260101_130000.json > comparison_report.txt
   ```

#### Seçenek B: Aynı OS, Farklı Kullanıcılar

İki farklı kullanıcı profilinde çalıştırın ve karşılaştırın.

## Adım Adım Çalıştırma

### Sistem 1 - Sizin Laptop'unuz

```bash
cd cs350project/src
python main.py
```

Giriş:
```
Enter folder path to scan (e.g., C:\ or /Users): C:\
```

Çıktı:
- Ekranda detaylı analiz
- Grafikler (PDF/CDF)
- JSON dosyası: `scan_results_windows_20260101_120000.json`

**Bu JSON dosyasını saklayın!** USB veya Google Drive ile arkadaşınıza gönderin.

### Sistem 2 - Arkadaşınızın Laptop'u

Aynı işlemi farklı bir bilgisayarda tekrarlayın:

```bash
cd cs350project/src
python main.py
```

Giriş (macOS):
```
Enter folder path to scan (e.g., C:\ or /Users): /Users
```

veya (Windows):
```
Enter folder path to scan (e.g., C:\ or /Users): C:\
```

**JSON dosyasını alın**: `scan_results_<sistem>_<timestamp>.json`

### Karşılaştırma

İki JSON dosyasını aynı klasöre koyun:

```bash
cd cs350project/src
python compare_systems.py scan_results_windows_20260101_120000.json scan_results_darwin_20260101_130000.json
```

Çıktı ekranda gösterilir. Kaydetmek için:

```bash
python compare_systems.py file1.json file2.json > comparison_report.txt
```

## Rapor İçin Gerekli Veriler

Hocanıza sunacağınız raporda şunlar olmalı:

### 1. Sistem Bilgileri
- Her iki sistemin OS, platform, mimari bilgisi
- Tarama tarihi ve süresi

### 2. Özet İstatistikler
- Toplam dosya sayısı
- Toplam disk kullanımı (GB)
- Unique extension sayısı

### 3. Top-20 File Extensions
- Dosya sayısına göre Top-20 (tabloda)
- Disk kullanımına göre Top-20 (tabloda)

### 4. Karşılaştırma
- İki sistem arasında ortak extension'lar
- Sadece bir sistemde olan extension'lar
- File type dağılımındaki farklar

### 5. PDF/CDF Grafikleri
- Her iki sistem için grafikleri rapora ekleyin
- Normal ve logaritmik ölçekleri gösterin

## Örnek Rapor Yapısı

```
CS350 PROJECT - FILE SYSTEM ANALYSIS REPORT

1. INTRODUCTION
   - Project goal
   - Systems analyzed

2. METHODOLOGY
   - Tools used (Python, numpy, matplotlib)
   - Scanning approach
   - Data collection process

3. SYSTEM 1 ANALYSIS
   - System info
   - Summary statistics
   - Top-20 extensions (by count)
   - Top-20 extensions (by size)
   - PDF/CDF graphs

4. SYSTEM 2 ANALYSIS
   - System info
   - Summary statistics
   - Top-20 extensions (by count)
   - Top-20 extensions (by size)
   - PDF/CDF graphs

5. COMPARISON
   - Side-by-side comparison table
   - Common vs unique extensions
   - Disk usage patterns
   - File size distributions

6. FINDINGS
   - Key observations
   - Differences between systems
   - Answer to analysis questions

7. CONCLUSION
```

## Olası Sorunlar ve Çözümler

### Sorun: "Permission Denied" hataları

**Çözüm**: Normal, bazı sistem dosyaları erişilebilir değil. Program bunları atlayarak devam eder.

### Sorun: Çok uzun sürüyor

**Çözüm**: Tam disk taraması 10-30 dakika sürebilir. Sabırlı olun.

### Sorun: JSON dosyası çok büyük

**Çözüm**: JSON sadece özet bilgi içerir, genelde < 1MB. Problem olmaz.

### Sorun: matplotlib kurulu değil

**Çözüm**:
```bash
pip install matplotlib
```

## İpuçları

1. **Test için önce küçük klasör**: Önce `C:\Users\YourName\Documents` gibi küçük bir klasörle test edin
2. **Sonra tam disk**: Çalıştığını gördükten sonra `C:\` veya `/Users` ile tam tarama yapın
3. **JSON'ları yedekleyin**: Tarama uzun sürebilir, JSON dosyalarını saklamak önemli
4. **Farklı bölümler**: Mimarlık, EE gibi farklı bölümlerden arkadaş bulmak ilginç sonuçlar verebilir

## Sorular?

Program çalışmazsa:
1. Python 3.x kurulu mu kontrol edin: `python --version`
2. Gerekli paketler kurulu mu: `pip list | grep numpy`
3. Dosya yolları doğru mu kontrol edin

## Son Kontrol Listesi

- [ ] İki farklı sistemde analiz yapıldı
- [ ] Her iki sistemin JSON dosyası var
- [ ] Top-20 file extensions raporu var
- [ ] Karşılaştırma raporu oluşturuldu
- [ ] PDF/CDF grafikleri kaydedildi
- [ ] Rapor yazıldı
