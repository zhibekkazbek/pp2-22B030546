import os
path = r"C:\Users\Сырым\Documents\pp2-22B030546\tsis6"

print(os.getcwd())
print(os.listdir('.'))
print(os.listdir(os.getcwd()))
os.chdir('./tests')
print(os.getcwd())