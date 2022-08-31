rows, colons = [int(x) for x in input().split(", ")]

matrix_list = [[int(x) for x in input().split(", ")] for row in range(rows)]
max_sum = {"max number": -181,
           "row": 0,
           "col": 0}


def check_valid_index(row, col):
    if 0 <= row + 2 <= rows and 0 <= col + 2 <= colons:
        return True


def sum_square(row, col):
    if check_valid_index(row, col):
        sum_total = 0
        for row_check in range(row, row + 2):
            sum_total += sum(matrix_list[row_check][col: col + 2])
        if max_sum["max number"] < sum_total:
            max_sum["max number"] = sum_total
            max_sum["row"] = row
            max_sum["col"] = col


for row in range(rows):
    for col in range(colons):
        sum_square(row, col)

for row in range(max_sum["row"], max_sum["row"] + 2):
    print(" ".join([str(x) for x in matrix_list[row][max_sum["col"]: max_sum["col"] + 2]]))
print(max_sum['max number'])