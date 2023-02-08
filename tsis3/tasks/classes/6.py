numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

# Using filter function with lambda to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list: ", prime_numbers)