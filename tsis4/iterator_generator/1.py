def generator(n):
    for i in range(n+1):
        yield i**2
for i in generator(int(input())):
    print(i)