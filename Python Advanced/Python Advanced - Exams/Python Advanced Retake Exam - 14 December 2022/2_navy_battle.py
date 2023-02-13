battlefield_size = int(input())

lives, enemy_cruiser, battlefield, submarine_row, submarine_col = 2, [], [], 0, 0
directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}


for x in range(battlefield_size):
    battlefield.append(list(input()))

    if "S" in battlefield[x]:
        submarine_row, submarine_col = x, battlefield[x].index("S")
        battlefield[submarine_row][submarine_col] = "-"

    if "C" in battlefield[x]:
        [enemy_cruiser.append([x, i]) for i in range(battlefield_size) if "C" == battlefield[x][i]]

while enemy_cruiser:

    if lives < 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
        break

    row_to_add, col_to_add = directions[input()]
    submarine_row, submarine_col = submarine_row + row_to_add, submarine_col + col_to_add

    if battlefield[submarine_row][submarine_col] == "*":
        lives -= 1

    elif battlefield[submarine_row][submarine_col] == "C":
        enemy_cruiser.remove([submarine_row, submarine_col])

    battlefield[submarine_row][submarine_col] = "-"

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

battlefield[submarine_row][submarine_col] = "S"
[print(*row, sep="") for row in battlefield]