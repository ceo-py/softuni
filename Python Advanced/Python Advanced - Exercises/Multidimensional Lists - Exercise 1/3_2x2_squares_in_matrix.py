rows, cols = [int(x) for x in input().split()]

square_matrix = [input().split() for _ in range(rows)]
all_square_matrices = []


def check_valid_index(row, col):
    if 0 <= row + 2 <= rows and 0 <= col + 2 <= cols:
        return True


def find_identical_chars(row, col):
    if check_valid_index(row, col):
        count_identical = 0
        symbol = square_matrix[row][col]
        for row_check in range(row, row + 2):
            count_identical += square_matrix[row_check][col:col + 2].count(symbol)
        if count_identical == 4:
            all_square_matrices.append(1)


for row in range(rows):
    for col in range(cols):
        find_identical_chars(row, col)

print(sum(all_square_matrices))
