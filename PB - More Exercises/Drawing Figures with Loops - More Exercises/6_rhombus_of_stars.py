number = int(input())

for row in range(1, number + 1):
    if row == 1:
        print((number - row) * " " + row * "*")
    else:
        print((number - row) * " " + row * "* ")

for rows in range(0, number - 1):
    if rows == 0:
        print((number - (row - 1)) * " " + (number - 1) * "* ")
    else:
        print((rows + 1) * " " + (number - rows - 1) * "* ")
