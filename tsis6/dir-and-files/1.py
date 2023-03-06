#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6"

print ("Only directories:")
a = []
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        a.append(name)
print(a)

print("\nOnly files:")
n = []
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        n.append(name)
print(n)

print("\nAll directories and files:")
m=[]
for name in os.listdir(path):
    m.append(name)
print(m)

"""
Only directories:
['builtin-functions', 'dir-and-files']

Only files:
['ex.py']

All directories and files:
['builtin-functions', 'dir-and-files', 'ex.py']"""