matrix = input().split("|")[::-1]

for row in range(len(matrix)):
    for num in matrix[row].split():
        print(num, end=" ")
