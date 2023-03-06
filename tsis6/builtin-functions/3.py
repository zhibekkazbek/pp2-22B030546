# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isPalindrome(s):
    return s == s[::-1]

s = input()

if isPalindrome(s):
    print("True")
else:
    print("False")