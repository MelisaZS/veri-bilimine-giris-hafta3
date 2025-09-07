# -*- coding: utf-8 -*-

# Soru 9 - Basit Çözüm (Numpy 1)

import numpy as np

# 1) 0–50 arası (dahil) 10 rastgele TAM sayı üret
dizi = np.random.randint(0, 51, size=10)   # üst sınır 51 -> 0..50 aralığı

# 2) İstenen istatistikler
ortalama = dizi.mean()  # aritmetik ortalama
std_sapma = dizi.std()  # numpy varsayılan
en_buyuk = dizi.max()    # maksimum değer

# 3) Sonuçlar
print("Dizi      :", dizi)
print("Ortalama  :", ortalama)
print("Std sapma :", std_sapma)
print("Maksimum  :", en_buyuk)
