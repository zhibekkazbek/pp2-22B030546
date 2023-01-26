x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

fruits = ("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')

fruits = ("apple", "banana", "cherry") # packing 
(green, yellow, red) = fruits # unpacking 
print(green)
print(yellow)
print(red)

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry") 
(green, *tropic, red) = fruits
print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry