# Write a Python program to split a string at uppercase letters.
# Напишите программу на Python для разделения строки на заглавные буквы.

import re

txt = "Kbtu a abb Abc"

x = re.split("[A-Z]", txt)
print(x)