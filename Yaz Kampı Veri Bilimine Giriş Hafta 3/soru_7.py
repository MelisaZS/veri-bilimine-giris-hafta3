# -*- coding: utf-8 -*-

# Soru 7 - (sorted + lambda)

kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]

# key= lambda s: len(s)  -> her kelimenin uzunluğunu anahtar olarak kullan
sirali = sorted(kelimeler, key=lambda s: len(s))

print(sirali)  # ['veri', 'bilim', 'python', 'analiz', 'yapayzeka']
