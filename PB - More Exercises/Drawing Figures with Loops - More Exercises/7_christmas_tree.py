number = int(input())

for row in range(0, number):
    if row == 0:
        print((number) * " " + " |")
        print((number - 1) * " " + "* | *")
    else:
        print((number - (row + 1)) * " " + (row + 1) * "*" + " | " + (row + 1) * "*")
