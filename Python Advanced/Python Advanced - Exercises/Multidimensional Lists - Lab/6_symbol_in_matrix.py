rows = int(input())
matrix = [input() for _ in range(rows)]
symbol_to_find = input()


def find_symbol(symbol):
    for row in range(rows):
        if symbol in matrix[row]:
            return row, matrix[row].find(symbol)
    return f"{symbol} does not occur in the matrix"


print(find_symbol(symbol_to_find))



# for row in range(rows):
#     if symbol_to_find in matrix[row]:
#         print(f"({row}, {matrix[row].index(symbol_to_find)})")
#         break
# else:
#     print(f"{symbol_to_find} does not occur in the matrix")
