MATRIX_SIZE = 6
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(MATRIX_SIZE)]
prize, total_score = "", [0]


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def get_score(col):
    for row in range(MATRIX_SIZE):
        symbol = matrix[row][col]
        total_score[0] += symbol


for throw in range(3):
    row, col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    if check_valid_index(row, col) and matrix[row][col] == "B":
        matrix[row][col] = 0
        get_score(col)

if 100 > total_score[0]:
    print(f"Sorry! You need {100 - total_score[0]} points more to win a prize.")
else:
    if 100 <= total_score[0] <= 199:
        prize = "Football"
    elif total_score[0] <= 299:
        prize = "Teddy Bear"
    elif total_score[0] >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {total_score[0]} points, and you've won {prize}.")
