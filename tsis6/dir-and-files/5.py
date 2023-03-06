# Write a Python program to write a list to a file.
list = ['apple', 'banana', 'orange']
path = r'C:\Users\Сырым\Documents\pp2-22B030546\tsis6\dir-and-files\abc.txt'
with open(path, 'w') as f:
    for element in list:
        f.write(element + '\n')