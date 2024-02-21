import datetime
def printdays():
    x = datetime.datetime.now().date() - datetime.timedelta(days=1)
    y = datetime.datetime.now().date()
    z = datetime.datetime.now().date() + datetime.timedelta(days=1)
    print(x, y, z)


printdays()