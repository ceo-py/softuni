rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
cols = len(matrix[0])


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    print("Invalid coordinates")


def add_to_matrix(row, col, value, operator):
    if check_valid_index(row, col):
        if "Add" in operator:
            matrix[row][col] += value
        else:
            matrix[row][col] -= value


command = input()
while command != "END":
    command_type, row, col, value = [int(x) if x[-1].isdigit() else x for x in command.split()]
    add_to_matrix(row, col, value, command_type)
    command = input()

[print(*matrix[row]) for row in range(rows)]
