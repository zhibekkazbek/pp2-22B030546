# If statement:

from this import d


a = 33
b = 200
if b > a:
  print("b is greater than a")
  
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# One line if statement:
if a > b: print("a is greater than b")

# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
  
# операторы if не могут быть пустыми, но если у вас по какой-либо причине есть оператор if без содержимого, 
# вставьте оператор pass, чтобы избежать получения ошибки.
a = 33
b = 200

if b > a:
  pass


# exersices 

a = 50
b = 10
if a > b:
  print("Hello World")
  
a = 50
b = 10
if a != b:
  print("Hello World")
  
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
  
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
  
if a == b and c == d:
  print("Hello")

if a == b or c == d:
  print("Hello")
  
if 5 > 2:
  print("Five is greater than two!")
  
if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")