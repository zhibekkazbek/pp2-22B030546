x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x)) # int
print(type(y)) # int
print(type(z)) # int

x = 1.10
y = 1.0
z = -35.59

print(type(x)) # float
print(type(y)) # float
print(type(z)) # float

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x)) # complex
print(type(y)) # complex
print(type(z)) # complex

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

import random
print(random.randrange(1, 10))

# exersices

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)