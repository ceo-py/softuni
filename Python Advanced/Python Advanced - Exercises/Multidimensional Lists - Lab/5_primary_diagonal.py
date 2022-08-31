rows = int(input())
matrix = [[x for x in input().split()] for _ in range(rows)]
[print(sum(int(matrix[i][i]) for i in range(rows)))]


