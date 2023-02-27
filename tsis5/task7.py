# Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(txt):
    return ''.join(x.capitalize() for x in txt.split('_'))

print(snake_to_camel('kbtu_fit'))