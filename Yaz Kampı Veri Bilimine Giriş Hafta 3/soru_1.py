# -*- coding: utf-8 -*-

# Soru 1

# Verilen not listesi
notlar = [85, 92, 76, 92, 100, 76, 85, 92]

# 1) Yinelenenleri kaldır (sıra korunsun)
benzersiz = []
for n in notlar:
    if n not in benzersiz:
        benzersiz.append(n)

# 2) En yüksek ve en düşük not
en_yuksek = max(notlar)
en_dusuk = min(notlar)

# 3) Küçükten büyüğe sıralama
sirali = sorted(notlar)

# Sonuçlar
print("Orijinal:", notlar)
print("Benzersiz:", benzersiz)
print("En yüksek:", en_yuksek)
print("En düşük:", en_dusuk)
print("Sıralı:", sirali)

