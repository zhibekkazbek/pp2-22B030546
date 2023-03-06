# Write a Python program to split a string at uppercase letters.
# Напишите программу на Python для разделения строки на заглавные буквы.

import re

txt = "Kbtu a abb Abc"

x = re.findall("[A-Z][a-z]+", txt)
print(x)