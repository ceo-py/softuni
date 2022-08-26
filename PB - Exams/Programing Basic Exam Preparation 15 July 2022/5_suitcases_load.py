lugged_capacity = float(input())

suitcases = 0
lugged = input()

while lugged != "End":
    lugged = float(lugged)
    suitcases += 1

    added_lugged_space = 0
    if suitcases % 3 == 0:
        added_lugged_space = lugged * 0.10

    lugged_capacity -= lugged + added_lugged_space

    if lugged_capacity <= 0:
        if lugged_capacity != 0:
            pass
            # suitcases -= 1
        print("No more space!")
        break

    lugged = input()

else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases} suitcases loaded.")
