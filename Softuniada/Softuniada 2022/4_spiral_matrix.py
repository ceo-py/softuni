rows, cols = [int(input()) for _ in range(2)]
matrix = [input().split() for _ in range(rows)]

while True:
    try:
        [print(matrix[0].pop(0), end = " ") for _ in range(len(matrix[0]))]
        del matrix[0]
        [print(matrix[r].pop(), end = " ") for r in range(len(matrix))]
        [print(matrix[len(matrix) - 1].pop(), end=" ") for _ in range(len(matrix[0]))]
        del matrix[-1]
        [print(matrix[r].pop(0), end=" ") for r in range(len(matrix) - 1, -1, -1)]
    except IndexError:
        break




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