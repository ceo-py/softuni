rows, cols = [int(input()) for _ in range(2)]
matrix = [input().split() for _ in range(rows)]

while True:
    try:
        [print(matrix[0].pop(0), end=" ") for _ in range(len(matrix[0]))]
        del matrix[0]
        [print(matrix[r].pop(), end=" ") for r in range(len(matrix))]
        [print(matrix[len(matrix) - 1].pop(), end=" ") for _ in range(len(matrix[0]))]
        del matrix[-1]
        [print(matrix[r].pop(0), end=" ") for r in range(len(matrix) - 1, -1, -1)]
    except IndexError:
        break




# def print_matrix_spiral(matrix, rows, cols):
#     # helper function to print a matrix in spiral way
#     def print_spiral(matrix, r1, r2, c1, c2):
#         if r1 > r2 or c1 > c2:
#             return
#
#         for c in range(c1, c2 + 1):
#             print(matrix[r1][c], end=" ")
#
#         for r in range(r1 + 1, r2 + 1):
#             print(matrix[r][c2], end=" ")
#
#         if r1 < r2 and c1 < c2:
#             for c in range(c2 - 1, c1, -1):
#                 print(matrix[r2][c], end=" ")
#             for r in range(r2, r1, -1):
#                 print(matrix[r][c1], end=" ")
#
#         print_spiral(matrix, r1 + 1, r2 - 1, c1 + 1, c2 - 1)
#
#     # main function to print the matrix in spiral way
#     if rows < 1 or cols < 1:
#         return
#     print_spiral(matrix, 0, rows - 1, 0, cols - 1)
#
#
# rows, cols = [int(input()) for _ in range(2)]
# matrix = [input().split() for _ in range(rows)]
# print_matrix_spiral(matrix, rows, cols)





#
# rows, cols = [int(input()) for _ in range(2)]
#
# matrix = [input().split() for _ in range(rows)]
#
#
# def print_spyral_matrix():
#     if matrix:
#         top = matrix[0]
#         del matrix[0]
#         print(*top, end=" ")
#     if matrix:
#         right = [matrix[r].pop() for r in range(len(matrix))]
#         print(*right, end=" ")
#     if matrix:
#         last_row = len(matrix) - 1
#         [print(matrix[last_row].pop(), end=" ") for _ in range(len(matrix[0]))]
#         del matrix[last_row]
#     if matrix:
#         rows_left = len(matrix) - 1
#         [print(matrix[r].pop(0), end=" ") for r in range(rows_left, -1, -1)]
#
#
# while matrix:
#     print_spyral_matrix()
