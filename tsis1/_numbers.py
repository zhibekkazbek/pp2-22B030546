x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))



#convert from int to float:
a = float(x) 

#convert from float to int:
b = int(y) 

#convert from int to complex:
c = complex(x) 

print(a) # 1.0
print(b) # 2
print(c) # (1+0j)

print(type(a))
print(type(b))
print(type(c))