rows, colons = [int(x) for x in input().split()]

matrix_list = [[int(x) for x in input().split()] for row in range(rows)]
max_sum = {"max number": -181,
           "row": 0,
           "col": 0}


def check_valid_index(row, col):
    if 0 <= row + 3 <= rows and 0 <= col + 3 <= colons:
        return True


def sum_rectangle(row, col):
    if check_valid_index(row, col):
        sum_total = 0
        for row_check in range(row, row + 3):
            sum_total += sum(matrix_list[row_check][col: col + 3])
        if max_sum["max number"] < sum_total:
            max_sum["max number"] = sum_total
            max_sum["row"] = row
            max_sum["col"] = col


for row in range(rows):
    for col in range(colons):
        sum_rectangle(row, col)

print(f"Sum = {max_sum['max number']}")
for row in range(max_sum["row"], max_sum["row"] + 3):
    print(" ".join([str(x) for x in matrix_list[row][max_sum["col"]: max_sum["col"] + 3]]))
