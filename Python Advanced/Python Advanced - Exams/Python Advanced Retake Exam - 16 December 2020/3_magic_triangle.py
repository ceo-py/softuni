def get_magic_triangle(rows):
    result = []
    for row in range(rows):
        result.append([])
        result[row].append(1)
        for col in range(1, row):
            result[row].append(result[row - 1][col - 1] + result[row - 1][col])
        if row != 0:
            result[row].append(1)
    return result

# Pascal’s Triangle in Python
get_magic_triangle(5)