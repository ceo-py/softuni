import math

number = int(input())

connection = math.ceil(number / 2)

for row in range(0, number):
    if connection == row + 1:
        print("*" + ((number * 2) - 2) * "/" + "*" + number * "|" + "*" + ((number * 2) - 2) * "/" + "*")
    elif row == 0 or number - 1 == row:
        print((number * 2) * "*" + number * " " + (number * 2) * "*")
    else:
        print("*" + ((number * 2) - 2) * "/" + "*" + number * " " + "*" + ((number * 2) - 2) * "/" + "*")
