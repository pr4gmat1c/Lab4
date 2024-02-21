def squares(n):
    for x in range(n+1):
        yield(x*x)


n = input("Enter number:")
n = int(n)
res = squares(n)
for x in res:
    print(x)
