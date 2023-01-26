# myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"} 
print(thisset) # {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
