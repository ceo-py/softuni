SIZE = int(input())
racing_number = input()
matrix, tunnel, row, col, kilometers = [], [], 0, 0, 0

for row_ in range(SIZE):
    matrix.append(input().split())

    if "T" in matrix[row_]:
        tunnel.append([row_, matrix[row_].index("T")])

command = input()

while command != "End":

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1

    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    step_on = matrix[row][col]

    if step_on == ".":
        kilometers += 10

    elif step_on == "T":
        kilometers += 30
        matrix[row][col] = "."
        tunnel.remove([row, col])
        row, col = tunnel[0]
        matrix[row][col] = "."

    elif step_on == "F":
        kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

matrix[row][col] = "C"

print(f"Distance covered {kilometers} km.")
[print(*row, sep="") for row in matrix]