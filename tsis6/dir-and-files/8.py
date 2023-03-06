# Write a Python program to delete file by specified path. Before deleting check for access and whether a 
# given path exists or not.
import os

if os.path.exists(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\D.txt"):
  os.remove(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\D.txt")
else:
  print("The file does not exist")