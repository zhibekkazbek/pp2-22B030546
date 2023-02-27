# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

txt = "kbtu ab abb abbb aba abba abc acd accc acddd a_ba a_v"
pattern = "[a-z]_[a-z]"
x = re.findall(pattern, txt)
print(x)