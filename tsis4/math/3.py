import math 
a = int(input())
b = int(input())
x = a * b**2 / (4 * math.tan(math.pi/a))
print(int(x))