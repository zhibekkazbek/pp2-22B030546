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

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
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

# Python также имеет множество встроенных функций, возвращающих логическое значение, таких 
# как функция isinstance(), которая может использоваться для определения того, 
# относится ли объект к определенному типу данных:
x = 200
print(isinstance(x, int))
