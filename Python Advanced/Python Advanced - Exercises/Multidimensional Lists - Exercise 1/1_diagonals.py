rows = int(input())

nested_list = [[int(x) for x in input().split(", ")] for _ in range(rows)]


def diagonal_sums(matrix, rows):
    diagonals = {
        "primary sum": [],
        "secondary sum": []
    }

    for i in range(rows):
        diagonals["primary sum"].append(matrix[i][i])
        diagonals["secondary sum"].append(matrix[i][rows - i - 1])

    print(
        f"Primary diagonal: {', '.join(str(x) for x in diagonals['primary sum'])}. Sum: {sum(diagonals['primary sum'])}")
    print(
        f"Secondary diagonal: {', '.join(map(str, diagonals['secondary sum']))}. Sum: {sum(diagonals['secondary sum'])}")


diagonal_sums(nested_list, rows)
