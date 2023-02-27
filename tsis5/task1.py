# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

txt = "kbtu ab abb abbb aba abba abc acd accc acddd"
pattern = r"ab*"
x = re.search(pattern, txt)
print(x)