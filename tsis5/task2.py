# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

txt = "kbtu ab abb abbb aba abba abc acd accc acddd"
pattern = r'a(bb|bbb)'

x = re.search(pattern, txt)
print(x)