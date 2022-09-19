from math import pi

a = input()
if a == "square":
    b = float(input())
    print(format(b*b, ".3f"))
elif a == "rectangle":
    b = float(input())
    c = float(input())
    print(format(b * c, ".3f"))
elif a == "circle":
    b = float(input())
    print(format(((pi) * b ** 2), ".3f"))
elif a == "triangle":
    b = float(input())
    c = float(input())
    print(format(b * c / 2, ".3f"))