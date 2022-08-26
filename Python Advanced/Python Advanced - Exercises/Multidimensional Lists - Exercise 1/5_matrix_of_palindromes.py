rows, cols = [int(x) for x in input().split()]

for row in range(97, 97 + rows):
    for col in range(97, 97 + cols):
        print(f"{chr(row)}{chr((row + col) - 97)}{chr(row)}", end=" ")
    print()
