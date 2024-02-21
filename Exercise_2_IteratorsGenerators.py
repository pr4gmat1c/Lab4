def evennum(n):
    for x in range(n+1):
        if x%2 == 0:
            yield(x)


n = input("Enter number:")
n = int(n)
res = evennum(n)
for x in res:
    print(x, end=", ")