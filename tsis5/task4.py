# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

txt = "Kbtu ab abb abbb aba Abba abc acd accc acddd a_ba a_v"
pattern = "[A-Z][a-z]"

x = re.findall(pattern, txt)
print(x)