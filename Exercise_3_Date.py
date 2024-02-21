import datetime
def nomicro():
    x = datetime.datetime.now()
    print(x.strftime("%c"))


nomicro()