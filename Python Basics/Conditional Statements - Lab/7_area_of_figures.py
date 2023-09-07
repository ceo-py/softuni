from math import pi

form = input()

if form == "square":
    b = float(input())
    print(format(b*b, ".3f"))

elif form == "rectangle":
    b = float(input())
    c = float(input())
    print(format(b * c, ".3f"))

elif form == "circle":
    b = float(input())
    print(format(((pi) * b ** 2), ".3f"))

elif form == "triangle":
    b = float(input())
    c = float(input())
    print(format(b * c / 2, ".3f"))