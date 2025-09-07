# -*- coding: utf-8 -*-

# Soru 8 - (metindeki sayı gruplarını topla)

def sayilari_topla(metin):
    toplam = 0          # bütün sayı gruplarının toplamı
    sayi = 0            # o an okunan sayı grubu (örn. '12' -> 1 sonra 12)
    aktif = False       # şu anda bir sayı grubunun içindeyiz mi?

    for ch in metin:
        if ch.isdigit(): # rakam gördükse
            sayi = sayi * 10 + int(ch)  # grubu büyüt (örn. 1 -> 12)
            aktif = True
        else:  # rakam değilse, varsa grubu toplama ekle
            if aktif:
                toplam += sayi
                sayi = 0
                aktif = False

    if aktif: # metin sayı ile bittiyse son grubu ekle
        toplam += sayi

    return toplam

# Hızlı testler
print(sayilari_topla("abc12def3"))  # 15
print(sayilari_topla("no digits"))  # 0
print(sayilari_topla("x007y5"))     # 12  (007 -> 7, 5 -> 5)

