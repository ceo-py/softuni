rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
print(sum(list(map(sum, zip(*matrix)))))
# print(sum([sum(idx) for idx in zip(*matrix)]))
print(matrix)