def divisible(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible(int(input())):
    print(num)            