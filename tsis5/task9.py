# Write a Python program to insert spaces between words starting with capital letters.
# Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.

import re 

txt = "KbtuFitKbtuFitMidterm"
pattern = r"([A-Z][a-z]+)"
x = re.sub(pattern, r" \1", txt).strip()
print(x)