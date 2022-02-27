number = int(input())

bonuses = {
    "100": 5,
    "over 100": 0.20,
    "over 1000": 0.10,
    "even": 1,
    "end on 5": 2
}
check_in_end_on_five = str(number)

if number <= 100:
    if (number % 2) == 0:
        bonus = bonuses["100"] + bonuses["even"]
        total = number + bonus
    elif check_in_end_on_five[-1] == "5":
        bonus = bonuses["end on 5"] + bonuses["100"]
        total = number + bonus
    else:
        bonus = bonuses["100"]
        total = number + bonus
elif number in range(100, 1000):
    if (number % 2) == 0:
        bonus = bonuses["over 100"] * number + bonuses["even"]
        total = number + bonus
    elif check_in_end_on_five[-1] == "5":
        bonus = bonuses["end on 5"] + bonuses["over 100"] * number
        total = number + bonus
    else:
        bonus = bonuses["over 100"] * number
        total = number + bonus
elif number > 1000:
    if (number % 2) == 0:
        bonus = bonuses["over 1000"] * number + + bonuses["even"]
        total = number + bonus
    elif check_in_end_on_five[-1] == "5":
        bonus = bonuses["end on 5"] + bonuses["over 1000"] * number
        total = number + bonus
    else:
        bonus = bonuses["over 1000"] * number
        total = number + bonus

print(f"{bonus}\n{total}")
