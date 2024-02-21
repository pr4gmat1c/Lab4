import datetime
def diffdate():
    x = datetime.datetime(2024, 2, 1)
    y = datetime.datetime(2024, 2, 19)
    z = y - x
    print(z.total_seconds())


diffdate()