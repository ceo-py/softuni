rows = int(int(input()))
matrix = [[x for x in input()] for _ in range(rows)]
cols = len(matrix[0])
total_knights = [0]


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


movement = {
    "up left": [-2, -1], "up right": [-2, 1],
    "down left": [2, -1], "down right": [2, 1],
    "left up": [-1, -2], "left down": [1, -2],
    "right up": [-1, 2], "right down": [1, 2],
}


def find_all_knights():
    positions = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "K":
                positions.append(row)
                positions.append(col)
    return positions


# while True:
#     pos_knights = find_all_knights()
#     result = {}
#     for i in range(0, len(pos_knights), 2):
#         row, col = pos_knights[i], pos_knights[i + 1]
#         for m_row, m_col in movement.values():
#             knight_row, knight_col = row + m_row, col + m_col
#             if check_valid_index(knight_row, knight_col):
#                 if matrix[knight_row][knight_col] == "K":
#                     result[f"{row} {col}"] = result.get(f"{row} {col}", 0) + 1
#     if sum(result.values()) == 0:
#         break
#     total_knights[0] += 1
#     row, col = max(result, key=result.get).split()
#     matrix[int(row)][int(col)] = "0"



def check_knights(pos_knights):
    result = {}
    for i in range(0, len(pos_knights), 2):
        row, col = pos_knights[i], pos_knights[i + 1]
        for m_row, m_col in movement.values():
            knight_row, knight_col = row + m_row, col + m_col
            if check_valid_index(knight_row, knight_col):
                if matrix[knight_row][knight_col] == "K":
                    result[f"{row} {col}"] = result.get(f"{row} {col}", 0) + 1
    if sum(result.values()) == 0:
        return
    total_knights[0] += 1
    row, col = max(result, key=result.get).split()
    matrix[int(row)][int(col)] = "0"
    check_knights(find_all_knights())


print(total_knights[0])

