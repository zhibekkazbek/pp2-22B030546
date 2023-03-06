# Write a Python program to convert a given camel case string to snake case.

import re

def func(Object):
    return Object.group("g1")+ "_" + Object.group("g2").lower()

txt = "camelCaseString"
pattern = r"(?P<g1>[a-z])(?P<g2>[A-Z])+"

print(re.sub(pattern, func, txt))