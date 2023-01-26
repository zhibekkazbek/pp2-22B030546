thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) # Mustang 

# There is also a method called get() that will give you the same result:
x = thisdict.get("model") # Mustang

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys() # dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
# dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(x) #after the change
# dict_keys(['brand', 'model', 'year', 'color'])


# The values() method will return a list of all the values in the dictionary.
x = thisdict.values() # dict_values(['Ford', 'Mustang', 1964])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
# dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x) #after the change
# dict_values(['Ford', 'Mustang', 2020])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
# dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
print(x) #after the change
# dict_values(['Ford', 'Mustang', 1964, 'red'])


# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["color"] = "red"
print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")