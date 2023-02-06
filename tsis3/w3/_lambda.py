# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

#_____________________________

# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

#_____________________________

# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#_____________________________

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

#_____________________________

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#_____________________________

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#_____________________________

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#_____________________________

# exersice 
x = lambda a : a

#_____________________________