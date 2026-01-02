# HIZLI BAŞLANGIÇ KILAVUZU - CS350 PROJECT

## Hocanın İstekleri ✓

1. ✅ Tüm disk analizi (C:\ veya /Users)
2. ✅ TOP-20 file extensions raporlama
3. ✅ İki farklı sistem/kullanıcı karşılaştırması
4. ✅ JSON export ve karşılaştırma araçları

## ADIM 1: Kendi Bilgisayarınızda Çalıştırın

```bash
cd src
python3 main.py
```

### Menü Seçenekleri:

Program size 3 seçenek sunar:

```
Scan Options:
  1. Quick scan - Enter a specific folder path
  2. Full disk scan - Scan entire system (recommended for project)
  3. Exit
```

**Proje için Seçenek 2'yi seçin!**

#### Seçenek 1: Quick Scan (Test için)
Belirli bir klasör girin:
- **Windows**: `C:\Users\YourName\Documents`
- **macOS**: `/Users/YourName/Documents`

#### Seçenek 2: Full Disk Scan (ÖNERİLİR - Hocanın istediği)
Program otomatik olarak tam diski tarar:
- **Windows**: `C:\` otomatik seçilir
- **macOS**: `/Users` otomatik seçilir
- **Linux**: `/home` otomatik seçilir

Onay ister: `Continue? (y/n)` → **y** yazın

### Çıktı:
- Ekranda detaylı analiz
- TOP-20 file extensions (sayı ve boyut)
- PDF/CDF grafikleri
- **JSON dosyası**: `scan_results_darwin_20260101_120000.json` (örnek)

**⚠️ ÖNEMLİ**: Bu JSON dosyasını saklayın!

## ADIM 2: Arkadaşınızın Bilgisayarında Çalıştırın

Kodları arkadaşınızın bilgisayarına kopyalayın (USB/email):

```bash
cd src
python main.py
```

Farklı bölümden arkadaş önerilir:
- Mimarlık öğrencisi
- Elektrik-Elektronik öğrencisi  
- Endüstri Mühendisliği öğrencisi

**Çıktı JSON**: `scan_results_windows_20260101_130000.json` (örnek)

## ADIM 3: Karşılaştırın

İki JSON dosyasını aynı klasöre koyun:

```bash
cd src
python compare_systems.py scan_results_darwin_20260101_120000.json scan_results_windows_20260101_130000.json
```

Çıktıyı dosyaya kaydetmek için:

```bash
python compare_systems.py file1.json file2.json > comparison_report.txt
```

## Proje Dosyaları

```
cs350project/
├── src/
│   ├── main.py                 # Ana program (buradan başlayın)
│   ├── scanner.py              # Disk tarayıcı
│   ├── analyze.py              # İstatistik analiz
│   ├── pdf_cdf.py             # PDF/CDF hesaplama
│   ├── plotter.py             # Grafik çizim
│   ├── export_results.py      # JSON export
│   └── compare_systems.py     # Sistem karşılaştırma
├── README.md                   # Detaylı dokümantasyon
├── USAGE_GUIDE.md             # Türkçe kullanım kılavuzu
└── QUICK_START.md             # Bu dosya
```

## Çıktı Örnekleri

### Terminal Çıktısı:
```
=== FILE EXTENSIONS ANALYSIS (TOP-20) ===
Total unique extensions: 247
Files without extension: 1234

Top 20 extensions by file count:
   1. .txt            :    12345 files ( 15.23%)
   2. .jpg            :     9876 files ( 12.18%)
   3. .pdf            :     8765 files ( 10.81%)
   ...

=== DISK USAGE BY EXTENSION (TOP-20) ===
   1. .mp4            :    45.23 GB (23.45%) |    1234 files | Avg:  37543.21 KB
   2. .zip            :    32.10 GB (16.65%) |     567 files | Avg:  58012.34 KB
   ...
```

### JSON Çıktısı:
```json
{
  "system_info": {
    "os": "Darwin",
    "platform": "macOS-14.0-arm64",
    "scan_date": "2026-01-01T12:00:00"
  },
  "summary": {
    "total_files": 123456,
    "total_size_gb": 256.78,
    "unique_extensions": 247
  },
  "top_20_extensions_by_count": [...],
  "top_20_extensions_by_size": [...]
}
```

## Rapor İçin Gerekli Veriler

Hocanıza sunacağınız raporda:

1. **İki Sistem Bilgisi**
   - OS, platform, tarih

2. **Her Sistem İçin**
   - Toplam dosya sayısı
   - Toplam disk kullanımı (GB)
   - TOP-20 extensions (sayı ve boyut tablosu)
   - PDF/CDF grafikleri

3. **Karşılaştırma**
   - Yan yana tablolar
   - Ortak/benzersiz extensions
   - Farklar ve benzerlikler

4. **Bulgular**
   - 90% of files < 100KB? (YES/NO)
   - Largest 10% = 90% disk? (YES/NO)

## Sorun Giderme

### `ModuleNotFoundError: No module named 'numpy'`
```bash
pip install numpy matplotlib
```

### `ModuleNotFoundError: No module named 'export_results'`
- `src/` klasöründe olduğunuzdan emin olun
- Tüm dosyaların src/ içinde olduğunu kontrol edin

### Çok uzun sürüyor
- Normal! Tam disk taraması 10-30 dakika sürebilir
- İlerlemeyi görmek için: her 5000 dosyada sayaç güncellenir

### Permission Denied hataları
- Normal! Bazı sistem dosyaları erişilemez
- Program bunları atlayıp devam eder

## Test İçin

İlk defa çalıştırıyorsanız, küçük bir klasörle test edin:

```bash
python main.py
# Input: C:\Users\YourName\Documents (Windows)
# Input: /Users/YourName/Documents (macOS)
```

Çalıştığını gördükten sonra tam disk taraması yapın.

## Checklist

- [ ] Kendi sistemimde analiz yaptım
- [ ] JSON dosyası oluşturuldu
- [ ] Arkadaşımın sisteminde analiz yaptım
- [ ] İkinci JSON dosyası aldım
- [ ] Karşılaştırma yaptım
- [ ] Grafikler kaydedildi
- [ ] Rapor yazıldı

## Destek

Sorularınız için:
- README.md: Detaylı teknik bilgi
- USAGE_GUIDE.md: Türkçe adım adım kılavuz
