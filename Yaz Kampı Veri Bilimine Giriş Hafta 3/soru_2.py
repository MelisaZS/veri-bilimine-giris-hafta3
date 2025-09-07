# -*- coding: utf-8 -*-

# Soru 2 - (Armstrong sayısı kontrolü: küpler)
# Amaç: Bir sayının basamaklarının küpleri toplamı sayının kendisine eşit mi? (Örn: 153 -> 1^3 + 5^3 + 3^3 = 153)

def armstrong_mu(sayi):
    """
    Basamak küplerinin toplamı sayının kendisine eşitse True döner, aksi halde False döner.
    Not: Bu sürüm, özellikle "küpler" tanımına göredir (3 basamaklı klasik Armstrong/Narcissistic test).
    Örn: 153 -> 1^3 + 5^3 + 3^3 = 153  => True
         123 -> 1^3 + 2^3 + 3^3 = 36   => False
    """
    toplam = 0                      # Basamak küpleri toplamını biriktireceğimiz değişken
    for ch in str(sayi):            # sayıyı stringe çevirip her karakteri (basamak) tek tek dolaş
        basamak = int(ch)           # karakteri tekrar tam sayıya çevir (örn. '5' -> 5)
        toplam += basamak ** 3      # ilgili basamağın KÜPÜNÜ toplama ekle
    return toplam == sayi           # toplam, sayının kendisine eşitse Armstrong kabul et

# Hızlı testler: Doğruluk kontrolü için örnek sayılar
# 153, 370, 371, 407 -> bilinen Armstrong sayıları (küplerle)
# 123 -> Armstrong değil
# 0, 1, 2 -> tek basamaklılar için 0^3=0, 1^3=1, 2^3=8 (0 ve 1 True, 2 False)
testler = [153, 370, 371, 407, 123, 0, 1, 2]

for t in testler:
    # Her test sayısı için fonksiyon sonucunu yazdır
    # Biçim: "sayı -> True/False"
    print(f"{t} -> {armstrong_mu(t)}")
