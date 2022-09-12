MATRIX_SIZE, black_pawn_row, black_pawn_col, white_pawn_row, white_pawn_col = 8, 0, 0, 0, 0
counter, matrix, pawns_info = 0, [], {
    "w": {"move": (-1, 0), "capture check": ((-1, -1), (-1, 1))},
    "b": {"move": (1, 0), "capture check": ((1, -1), (1, 1))},
    "pawns": {"w": "b", "b": "w"},
    "print name": {"w": "White", "b": "Black"}

}

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "b" in matrix[row]:
        black_pawn_row, black_pawn_col = row, matrix[row].index("b")
    elif "w" in matrix[row]:
        white_pawn_row, white_pawn_col = row, matrix[row].index("w")


def get_position(row, col):
    for r_check_pos, r_swap_pos in ((8, 1), (-1, 8)):
        if r_check_pos == row:
            row = r_swap_pos
    for c_check_pos, c_swap_pos in ((8, 7), (-1, 0)):
        if c_check_pos == col:
            col = c_swap_pos
    return row, col


def check_valid_index(row, col, player, check_capture=True):
    if 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE:
        return True
    if not check_capture:
        winner(row, col, player)


def winner(row, col, player):
    print_row, print_col = get_position(row, col)
    print(
        f"Game over! {pawns_info['print name'][player]} pawn is promoted "
        f"to a queen at {chr(97 + print_col)}{print_row}.")
    exit()


def pawn_movement(row, col, player):
    return row + pawns_info[player]["move"][0], col + pawns_info[player]["move"][1]


def check_for_capture(row, col, player):
    for capture_row, capture_col in pawns_info[player]["capture check"]:
        p_check_row, p_check_col = row + capture_row, col + capture_col
        if check_valid_index(p_check_row, p_check_col, player) and \
                matrix[p_check_row][p_check_col] == pawns_info["pawns"][player]:
            print(
                f"Game over! {pawns_info['print name'][player]} win, "
                f"capture on {chr(97 + p_check_col)}{abs(p_check_row - 8)}.")
            exit()


def player_moves(row, col, player):
    matrix[row][col] = "-"
    check_for_capture(row, col, player)
    new_row, new_col = pawn_movement(row, col, player)
    check_valid_index(new_row, new_col, player, False)
    matrix[new_row][new_col] = player
    return new_row, new_col


while True:
    counter += 1

    if counter % 2 != 0:
        white_pawn_row, white_pawn_col = player_moves(white_pawn_row, white_pawn_col, "w")

    else:
        black_pawn_row, black_pawn_col = player_moves(black_pawn_row, black_pawn_col, "b")


'''
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
'''
#
#
#
#
#
# MATRIX_SIZE, black_pawn_row, black_pawn_col, white_pawn_row, white_pawn_col = 8, 0, 0, 0, 0
# counter, matrix, pawns_info = 0, [], {
#     "w": {"move": (-1, 0), "capture check": ((-1, -1), (-1, 1))},
#     "b": {"move": (1, 0), "capture check": ((1, -1), (1, 1))},
#     "pawns": {"w": "b", "b": "w"},
#     "print name": {"w": "White", "b": "Black"}
#
# }
#
# for row in range(MATRIX_SIZE):
#     matrix.append(input().split())
#     if "b" in matrix[row]:
#         black_pawn_row, black_pawn_col = row, matrix[row].index("b")
#     elif "w" in matrix[row]:
#         white_pawn_row, white_pawn_col = row, matrix[row].index("w")
#
#
# def get_position(row, col):
#     for r_check_pos, r_swap_pos in ((8, 1), (-1, 8)):
#         if r_check_pos == row:
#             row = r_swap_pos
#     for c_check_pos, c_swap_pos in ((8, 7), (-1, 0)):
#         if c_check_pos == col:
#             col = c_swap_pos
#     return row, col
#
#
# def check_valid_index(row, col, player, check_capture=True):
#     if 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE:
#         return True
#     if not check_capture:
#         winner(row, col, player)
#
#
# def winner(row, col, player):
#     print_row, print_col = get_position(row, col)
#     print(
#         f"Game over! {pawns_info['print name'][player]} pawn is promoted "
#         f"to a queen at {chr(97 + print_col)}{print_row}.")
#     exit()
#
#
# def pawn_movement(row, col, player):
#     return row + pawns_info[player]["move"][0], col + pawns_info[player]["move"][1]
#
#
# def check_for_capture(row, col, player):
#     for capture_row, capture_col in pawns_info[player]["capture check"]:
#         p_check_row, p_check_col = row + capture_row, col + capture_col
#         if check_valid_index(p_check_row, p_check_col, player) and \
#                 matrix[p_check_row][p_check_col] == pawns_info["pawns"][player]:
#             print(
#                 f"Game over! {pawns_info['print name'][player]} win, "
#                 f"capture on {chr(97 + p_check_col)}{abs(p_check_row - 8)}.")
#             exit()
#
#
# while True:
#     counter += 1
#     if counter % 2 != 0:
#         matrix[white_pawn_row][white_pawn_col] = "-"
#         check_for_capture(white_pawn_row, white_pawn_col, "w")
#         white_pawn_row, white_pawn_col = pawn_movement(white_pawn_row, white_pawn_col, "w")
#         check_valid_index(white_pawn_row, white_pawn_col, "w", False)
#         matrix[white_pawn_row][white_pawn_col] = "w"
#     else:
#         matrix[black_pawn_row][black_pawn_col] = "-"
#         check_for_capture(black_pawn_row, black_pawn_col, "b")
#         black_pawn_row, black_pawn_col = pawn_movement(black_pawn_row, black_pawn_col, "b")
#         check_valid_index(black_pawn_row, black_pawn_col, "b", False)
#         matrix[black_pawn_row][black_pawn_col] = "b"
#
# '''
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
# '''
