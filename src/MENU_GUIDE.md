# YENİ MENÜ SİSTEMİ - Kullanım Kılavuzu

## Güncelleme Özeti

Artık program çalıştığında kullanıcıya **3 seçenek** sunuluyor:

```
======================================================================
FILE SYSTEM ANALYZER - CS350 PROJECT
======================================================================

System: Darwin (macOS-26.2-arm64-arm-64bit)
Architecture: arm64
Date: 2026-01-02 12:00:00
======================================================================

Scan Options:
  1. Quick scan - Enter a specific folder path
  2. Full disk scan - Scan entire system (recommended for project)
  3. Exit

Select option (1/2/3): _
```

## Seçenek Açıklamaları

### 1️⃣ Quick Scan (Hızlı Tarama)
**Ne zaman kullanılır:** Test için, belirli bir klasör taramak için

**Nasıl çalışır:**
- Kullanıcı manuel olarak klasör yolu girer
- Örnek: `/Users/mirkaygusuz/Documents`
- Örnek: `C:\Users\YourName\Desktop`

**Örnek kullanım:**
```
Select option (1/2/3): 1

Enter folder path to scan: /Users/mirkaygusuz/Documents
```

### 2️⃣ Full Disk Scan (Tam Disk Taraması) - ÖNERİLİR
**Ne zaman kullanılır:** Hocanın istediği proje için

**Nasıl çalışır:**
- Program otomatik olarak işletim sistemini algılar
- Uygun tam disk yolunu otomatik seçer
- Kullanıcıdan onay ister

**İşletim sistemine göre otomatik yollar:**
- **Windows** → `C:\`
- **macOS** → `/Users`
- **Linux** → `/home`

**Örnek kullanım (macOS):**
```
Select option (1/2/3): 2

[INFO] Full disk scan selected: /Users
This will scan entire /Users directory. Continue? (y/n): y

[INFO] Scanning directory: /Users
[WARNING] Full disk scan may take 10-30 minutes...
```

**Örnek kullanım (Windows):**
```
Select option (1/2/3): 2

[INFO] Full disk scan selected: C:\
This will scan entire C:\ drive. Continue? (y/n): y

[INFO] Scanning directory: C:\
[WARNING] Full disk scan may take 10-30 minutes...
```

### 3️⃣ Exit (Çıkış)
Programdan çıkar.

## Güvenlik Özellikleri

1. **Onay Mekanizması:** Full disk scan seçildiğinde onay ister
2. **Bilgilendirme:** Hangi klasörün taranacağı gösterilir
3. **İptal Seçeneği:** `n` yazarsanız tarama iptal edilir
4. **OS Tespiti:** Yanlış yol girmekten korur

## Örnek Kullanım Senaryoları

### Senaryo 1: İlk Test
```bash
cd src
python3 main.py
# Seçenek: 1
# Yol: /Users/mirkaygusuz/Documents
# → Hızlı test, küçük veri
```

### Senaryo 2: Proje için Asıl Tarama
```bash
cd src
python3 main.py
# Seçenek: 2
# Onay: y
# → Tam disk taraması (hocanın istediği)
```

### Senaryo 3: Programdan Çıkış
```bash
cd src
python3 main.py
# Seçenek: 3
# → Goodbye!
```

## Eski Versiyon ile Fark

### Eski Versiyon:
```
Enter folder path to scan (e.g., C:\ or /Users): _
```
Kullanıcı her zaman manuel yol girmek zorunda.

### Yeni Versiyon:
```
Scan Options:
  1. Quick scan - Enter a specific folder path
  2. Full disk scan - Scan entire system (recommended for project)
  3. Exit

Select option (1/2/3): 2
```
Kullanıcı sadece "2" yazıyor, program otomatik işletim sistemini algılıyor.

## Avantajları

✅ Kullanıcı dostu menü  
✅ Otomatik OS algılama  
✅ Yanlış yol girme riski yok  
✅ Onay mekanizması ile güvenlik  
✅ Test ve asıl tarama ayrımı net  
✅ Proje için ideal ("2" seçeneği)  

## Hocanıza Gösterirken

1. **Menü ekranı screenshotu** gösterin
2. **Seçenek 2'yi** vurgulayın (Full disk scan)
3. **Otomatik OS algılamayı** gösterin
4. **Onay mekanizmasını** gösterin

Böylece programın profesyonel ve kullanıcı dostu olduğunu göstermiş olursunuz!

