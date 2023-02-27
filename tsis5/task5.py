# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# Напишите программу на Python, которая соответствует строке, за которой следует 'a', 
# за которой следует что угодно, заканчивающееся на 'b'

import re 

txt = "Kbtu a abb abbb aba Abba abc acd accc acddd ab"
pattern = 'a.*b$'
x = re.search(pattern, txt)

print(x) # <re.Match object; span=(5, 46), match='a abb abbb aba Abba abc acd accc acddd ab'>