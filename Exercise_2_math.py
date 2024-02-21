def trapezoid(a, b, h):
    area = (int(a)+int(b))/2 * int(h)
    print("Area of trapezoid is: ", area)


h = input("Enter height:")
a = input("Enter first value:")
b = input("Enter second value:")
trapezoid(a, b, h)