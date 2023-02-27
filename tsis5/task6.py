# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
# Напишите программу на Python, которая заменит все вхождения пробела, запятой или точки двоеточием.

import re
txt = "Kbtu a abb abbb aba Abba abc acd accc acddd ab ,a.b.ab"
pattern = "[ .,]"
x = re.sub(pattern, ":", txt)

print(x)