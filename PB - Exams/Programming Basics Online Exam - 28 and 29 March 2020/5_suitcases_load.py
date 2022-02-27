capacity_lagges = float(input())
number_lagges = 0
check_space = 0


while True:
    lagge = input()

    if "End" in lagge:
        print(f"Congratulations! All suitcases are loaded!\nStatistic: {number_lagges} suitcases loaded.")
        break

    number_lagges += 1
    lagges = float(lagge)
    check_space += + lagges

    if number_lagges % 3 == 0:
        check_space += lagges * 0.10

    if capacity_lagges < check_space:
        number_lagges += - 1
        print(f"No more space!\nStatistic: {number_lagges} suitcases loaded.")
        break
