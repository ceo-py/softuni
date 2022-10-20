SIZE = 6
matrix = [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(SIZE)]
total_sum = 0

for trow in range(3):
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    try:
        symbol = matrix[row][col]
    except IndexError:
        continue

    if symbol == "B":
        matrix[row][col] = 0
        for c_row in range(SIZE):
            total_sum += matrix[c_row][col]

if total_sum < 100:
    print(f"Sorry! You need {100-total_sum} points more to win a prize.")

else:
    if total_sum < 200:
        toy = "Football"
    elif total_sum < 300:
        toy = "Teddy Bear"
    elif total_sum >= 300:
        toy = "Lego Construction Set"
    print(f"Good job! You scored {total_sum} points, and you've won {toy}.")





#
# MATRIX_SIZE = 6
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(MATRIX_SIZE)]
# prize, total_score = "", [0]
#
#
# def check_valid_index(row, col):
#     return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE
#
#
# def get_score(col):
#     for row in range(MATRIX_SIZE):
#         symbol = matrix[row][col]
#         total_score[0] += symbol
#
#
# for throw in range(3):
#     row, col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
#     if check_valid_index(row, col) and matrix[row][col] == "B":
#         matrix[row][col] = 0
#         get_score(col)
#
# if 100 > total_score[0]:
#     print(f"Sorry! You need {100 - total_score[0]} points more to win a prize.")
# else:
#     if 100 <= total_score[0] <= 199:
#         prize = "Football"
#     elif total_score[0] <= 299:
#         prize = "Teddy Bear"
#     elif total_score[0] >= 300:
#         prize = "Lego Construction Set"
#     print(f"Good job! You scored {total_score[0]} points, and you've won {prize}.")
