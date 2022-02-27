player_name = input()

darts_info = {
    "Single": 1,
    "Double": 2,
    "Triple": 3
}

points_left = 301
trow_count = 0
check_for_score = 0
unsuccessful_trow = 0
points = 0

while True:
    field = input()

    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_trow} unsuccessful shots.")
        break

    else:
        points = int(input())

    check_for_score = points_left - darts_info[field] * points

    if check_for_score == 0:
        trow_count += 1
        print(f"{player_name} won the leg with {trow_count} shots.")
        break

    elif check_for_score >= 0:
        trow_count += 1
        points_left += - darts_info[field] * points

        if check_for_score == 0 or points_left == 0:
            print(f"{player_name} won the leg with {trow_count} shots.")
            break

    else:
        check_for_score = points_left
        unsuccessful_trow += 1
