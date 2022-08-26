rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]


def check_valid_index(row1, col1, row2, col2):
    if 0 <= row1 < rows and 0 <= col1 < cols \
            and 0 <= row2 < rows and 0 <= col2 < cols:
        return True
    print("Invalid input!")


def swap_command(row1, col1, row2, col2):
    if check_valid_index(row1, col1, row2, col2):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(len(matrix)):
            print(" ".join(map(str, matrix[row])))


command = input()
while command != "END":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split()]
    if "swap" == command_type and len(info) == 4:
        row1, col1, row2, col2 = info
        swap_command(row1, col1, row2, col2)
    else:
        print("Invalid input!")
    command = input()
