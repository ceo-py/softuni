number = int(input())

for row in range(1, number + 1):
    if row == 1 or number == row:
        print("+ " + (number - 2) * "- " + "+ ")
    else:
        print("| " + (number - 2) * "- " + "| ")
