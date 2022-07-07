board_len = 8
ches_board = []
for row in range(board_len):
    ches_board.append(["-" for _ in range(board_len)])


def show_board(ches_board):
    for row in ches_board:
        print(" ".join(row))
    print()


def queen_place(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal):
    if row in set_rows or col in set_cols or (row + col) in set_r_diagonal or (row - col) in set_l_diagonal:
        return False
    return True


def add_queen(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board):
    ches_board[row][col] = "*"
    set_rows.add(row)
    set_cols.add(col)
    set_l_diagonal.add(row - col)
    set_r_diagonal.add(row + col)


def remove_queen(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board):
    ches_board[row][col] = "-"
    set_rows.remove(row)
    set_cols.remove(col)
    set_l_diagonal.remove(row - col)
    set_r_diagonal.remove(row + col)


def check_board(row, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board):
    if row == board_len:
        show_board(ches_board)
        return

    for col in range(board_len):
        if queen_place(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal):
            add_queen(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board)
            check_board(row + 1, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board)
            remove_queen(row, col, set_rows, set_cols, set_l_diagonal, set_r_diagonal, ches_board)


check_board(0, set(), set(), set(), set(), ches_board)
