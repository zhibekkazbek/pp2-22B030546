# Write a Python program to convert a given camel case string to snake case.

import re

txt = "camelCaseString"
pattern = r"(?<!^)(?=[A-Z])"
snake = re.sub(pattern, '_', txt).lower()

print(snake)