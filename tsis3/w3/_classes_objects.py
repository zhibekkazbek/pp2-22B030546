# A Class is like an object constructor, or a "blueprint" for creating objects.
class MyClass:
    x = 5
    
#_____________________________

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) # 5

#_____________________________

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

#_____________________________

# The __str__() function controls what should be returned when the class object is represented as a string.

# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)
print(p1) # <__main__.Person object at 0x15039e602100>

#_____________________________

# The string representation of an object WITH the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1) # John(36)

#_____________________________

# Object Methods
# Методы в объектах - это функции, которые принадлежат объекту.
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("John", 36)
p1.myfunc()

#_____________________________

# selfПараметр является ссылкой на текущий экземпляр класса и используется для доступа к переменным, 
# которые принадлежат классу.

# It does not have to be named self , you can call it whatever you like, but it has to be the first 
# parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#_____________________________

# Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#_____________________________

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age) # AttributeError: 'Person' object has no attribute 'age'

#_____________________________

class Person:
  pass

#_____________________________

# exersices 

class MyClass:
  x = 5
  
#_____________________________

class MyClass:
  x = 5

p1 = MyClass()

#_____________________________

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

#_____________________________

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
#_____________________________