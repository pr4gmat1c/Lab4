import math
def polygon(s, l):
    area = (int(s) * int(l)*int(l) * (1/4)*(math.cos((math.pi/int(s)))/math.sin((math.pi/int(s)))))
    print("Area of the polygon is: ", area)


s = input("Enter number of sides:")
l = input("Enter the length of the side:")
polygon(s, l)
