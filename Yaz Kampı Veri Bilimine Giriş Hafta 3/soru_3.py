# -*- coding: utf-8 -*-

# Soru 3 - (Kümeler)

# Verilen kümeler
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

# 1) Ortak diller (kesişim)
ortak = A & B  # A.intersection(B) ile aynı

# 2) Sadece A'da olan diller (fark)
sadece_A = A - B  # A.difference(B) ile aynı

# 3) Birleşim (alfabetik yazdır)
birlesim_alfabetik = sorted(A | B)  # set birleşimi -> liste halinde alfabetik

# Sonuçları yazdır
print("Ortak diller:", ortak)
print("Sadece A'da olanlar:", sadece_A)
print("Birleşim (alfabetik):", birlesim_alfabetik)
