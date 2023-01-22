print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Evaluate Values and Variables
print(bool("Hello")) # true
print(bool(15)) # true

x = "Hello"
y = 15

print(bool(x)) # true
print(bool(y)) # true

# True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an 
# object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) # false

def myFunction() :
  return True

print(myFunction()) # true

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") # YES!

# Python также имеет множество встроенных функций, возвращающих логическое значение, таких 
# как функция isinstance(), которая может использоваться для определения того, 
# относится ли объект к определенному типу данных:
x = 200
print(isinstance(x, int)) # true


# exersices

print(10 > 9)
True

print(10 == 9)
False

print(10 < 9)
False

print(bool("abc"))
True

print(bool(0))
False