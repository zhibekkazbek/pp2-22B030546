# Write a Python program with builtin function that accepts a string and calculate the number of
# upper case letters and lower case letters

string = "KBTUfit"
cnt1 = 0
cnt2 = 0
for i in string:
    if(i.islower()):
        cnt1 += 1
    elif(i.isupper()):
        cnt2 += 1
print("Lowercase letter quantity:", cnt1)
print("Uppercase letter quantity:", cnt2)