import math
def radian(n):
    radian = (math.pi/180) * int(n)
    print("Conversion of degree to radian is: ", radian)

n = input("Enter degree:")
radian(n)