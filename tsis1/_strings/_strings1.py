# 'hello' is the same as "hello"
print("Hello")
print('Hello')

a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)
    
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword "in"
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt) # will be True

# Use it in an "if" statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") 
  
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt) # will be True

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")