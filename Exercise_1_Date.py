import datetime
def subtract5days():
    x = datetime.datetime.now().date() - datetime.timedelta(days=5)
    print(x)


subtract5days()