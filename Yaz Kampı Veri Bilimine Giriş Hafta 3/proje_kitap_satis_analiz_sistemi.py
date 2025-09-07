# -*- coding: utf-8 -*-

"""
Proje – Özet Gereksinimler (Basit Sürüm)
1) Fonksiyonlar:
   - en_cok_satan(kitaplar): En yüksek "satis" değerine sahip kitabı döndür.
   - yazar_satislari(kitaplar): Her yazarın toplam satışını döndür.
2) Kümeler / Listeler:
   - Tüm türleri KÜME olarak çıkar (tekrarsız).
   - Satışı 1000’den büyük kitap adlarını listele.
3) Lambda / Filter / Map / Sorted:
   - 2020’den sonra çıkan kitapları FILTER ile süz.
   - Satışları %10 artırılmış yeni listeyi MAP ile üret.
   - Kitapları SATIŞA göre AZALAN sırala (sorted + lambda).
4) İstatistik:
   - Ortalama satış ve standart sapma (statistics).
"""

# --- Örnek veri ---
kitaplar = [
    {"isim": "Veri Bilimi 101",         "yazar": "Ali",  "tur": "Bilim",    "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka",   "yazar": "Ayşe", "tur": "Bilim",    "satis": 950,  "yil": 2020},
    {"isim": "İstatistik Temelleri",    "yazar": "Ali",  "tur": "Akademik", "satis": 700,  "yil": 2019},
    {"isim": "Makine Öğrenmesi",        "yazar": "Can",  "tur": "Bilim",    "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme",     "yazar": "Deniz","tur": "Sanat",    "satis": 400,  "yil": 2018},
    {"isim": "Matematiksel Modelleme",  "yazar": "Ali",  "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu",           "yazar": "Ayşe", "tur": "Sosyal",   "satis": 600,  "yil": 2022},
]

# --- 1) Fonksiyonlar ---
def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda k: k["satis"])

def yazar_satislari(kitaplar):
    son = {}
    for k in kitaplar:
        y = k["yazar"]
        son[y] = son.get(y, 0) + k["satis"]
    return son

# --- 2) Kümeler / Listeler ---
turler = {k["tur"] for k in kitaplar}
bin_ustu = [k["isim"] for k in kitaplar if k["satis"] > 1000]

# --- 3) Lambda / Filter / Map / Sorted ---
yil_2020_sonrasi = list(filter(lambda k: k["yil"] > 2020, kitaplar))
satislar_yuzde10 = list(map(lambda k: int(round(k["satis"] * 1.10)), kitaplar))
azalan = sorted(kitaplar, key=lambda k: k["satis"], reverse=True)

# --- 4) İstatistik ---
import statistics as stats
satislar = [k["satis"] for k in kitaplar]
ortalama = stats.mean(satislar)
std = stats.stdev(satislar)  # örneklem std

# --- Çıktı ---
print("En çok satan:", en_cok_satan(kitaplar))
print("Yazar satışları:", yazar_satislari(kitaplar))
print("Türler:", turler)
print("1000+ satan kitaplar:", bin_ustu)
print("2020 sonrası:", [k["isim"] for k in yil_2020_sonrasi])
print("Satışlar %10 artış:", satislar_yuzde10)
print("Satışa göre azalan:", [k["isim"] for k in azalan])
print("Ortalama satış:", round(ortalama, 2))
print("Standart sapma:", round(std, 2))
