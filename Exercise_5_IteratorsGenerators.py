def nums(n):
    for x in range(n, -1, -1):
        yield(x)


n = input("Enter number:")
n = int(n)
res = nums(n)
for x in res:
    print(x, end=" ")