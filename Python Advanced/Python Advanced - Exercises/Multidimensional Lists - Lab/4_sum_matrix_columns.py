rows, cols = [int(x) for x in input().split(", ")]
result = list(map(sum, zip(*[[int(x) for x in input().split()] for _ in range(rows)])))
[print(x) for x in result]
