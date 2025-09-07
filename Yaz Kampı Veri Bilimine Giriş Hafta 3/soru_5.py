# -*- coding: utf-8 -*-

# Soru 5 
def kelime_sayaci(metin):
    # Sadelik için: sadece boşluklara göre bölüyoruz
    k = metin.lower().split()
    if not k:
        return 0, None, None

    # En uzun kelime
    en_uzun = max(k, key=len)

    # En sık kelime (manuel sayım)
    sayim = {}
    for w in k:
        sayim[w] = sayim.get(w, 0) + 1
    en_sik = max(sayim, key=sayim.get)

    # Toplam kelime sayısı, en uzun kelime, en sık kelime
    return len(k), en_uzun, en_sik

# Kısa test
m = "Veri bilimi, veri analizi ve Python! Veri veridir."
print(kelime_sayaci(m))
