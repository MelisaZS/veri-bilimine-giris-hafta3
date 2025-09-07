# -*- coding: utf-8 -*-

# Soru 10 -(NumPy 2)

import numpy as np

# 1) 5x5 boyutunda 0–1 arası (0 dahil, 1 hariç) rastgele sayılar
M = np.random.rand(5, 5)

# 2) Her sütunun ortalaması (axis=0 sütun yönü)
sutun_ort = M.mean(axis=0)

# 3) 0.5'ten büyükleri 1, küçük/eşit olanları 0 yap (binary matris)
binary = (M > 0.5).astype(int)

# Sonuçları yazdır
print("Matris (5x5):\n", M)
print("\nSütun ortalamaları:\n", sutun_ort)
print("\nBinary matris (eşik=0.5):\n", binary)
