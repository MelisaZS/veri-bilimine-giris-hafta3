# -*- coding: utf-8 -*-

# Soru 6 - Basit Çözüm (map, filter, sorted)

sayilar = [5, 12, 7, 18, 24, 3, 16]

# 1) Sadece çift sayıları filtrele
ciftler = list(filter(lambda n: n % 2 == 0, sayilar)) # -> [12, 18, 24, 16]

# 2) Bu sayıların karelerini al
kareler = list(map(lambda n: n * n, ciftler)) # -> [144, 324, 576, 256]

# 3) Kareleri azalan sırada sırala
sonuc = sorted(kareler, reverse=True) # -> [576, 324, 256, 144]

print("Çiftler    :", ciftler)
print("Kareler    :", kareler)
print("Azalan sıralı:", sonuc)

