# Global Variables
# Global variables can be used by everyone, both inside of functions and outside.

x = 'awesome'

def myfunc():
    x = "fantastic"
    print('Python is ' + x)

myfunc()

print("Python is " + x)

# The global Keyword
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = 'fantastic'
    
myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)