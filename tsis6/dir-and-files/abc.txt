#Write a Python program to check for access to a specified path. Test the existence, readability, 
# writability and executability of the specified path
import os
print('Exist:', os.access(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\dir-and-files", os.F_OK))
print('Readable:', os.access(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\dir-and-files", os.R_OK))
print('Writable:', os.access(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\dir-and-files", os.W_OK))
print('Executable:', os.access(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6\dir-and-files", os.X_OK))
