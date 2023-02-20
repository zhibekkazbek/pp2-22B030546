def even_numbers(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num

n = int(input())
even = even_numbers(n)

for num in even:
    print(num, end=", ")