thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# add new item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


for x in thisdict:
  print(x)
  
# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
  
# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
  
# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
  
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)