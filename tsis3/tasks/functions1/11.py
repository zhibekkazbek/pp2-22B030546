def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam")) # Output: True
print(is_palindrome("hello")) # Output: False
print(is_palindrome(str("abc cba"))) # Output: True