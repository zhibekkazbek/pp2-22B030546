fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for x in "banana":
  print(x)
  
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # apple cherry
  
for x in range(6):
  print(x) # 0 1 2 3 4 5 
  
for x in range(2, 6):
  print(x) # 2 3 4 5
  
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x) # 2 5 8 11 14 17 20 23 26 29
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") # 0 1 2 
  #If the loop breaks, the else block is not executed.
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    # red apple
    # red banana
    # red cherry
    # big apple
    # big banana
    # big cherry
    # tasty apple
    # tasty banana
    # tasty cherry

for x in [0, 1, 2]:
  pass