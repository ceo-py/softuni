rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]

movement = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}

print(matrix)
