# -*- coding: utf-8 -*-

# Soru 4 
import random, statistics as stats

sayilar = [random.randint(1, 100) for _ in range(10)]  # 10 rastgele sayı
print("Sayılar:", sayilar)
print("Ortalama:", stats.mean(sayilar))
print("Standart sapma:", stats.stdev(sayilar))  

