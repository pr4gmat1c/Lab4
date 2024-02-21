def squares(a, b):
    for x in range(a, b+1):
        yield(x*x)


a = input("Enter number:")
b = input("Enter number:")
a = int(a)
b = int(b)
res = squares(a, b)
for x in res:
    print(x)