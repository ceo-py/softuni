dancers_number = int(input())
number_points = float(input())
season = input()
place = input()

off = 0
is_bulgaria = False
if season == "summer":
    if place == "Bulgaria":
        is_bulgaria = True
        off = 0.05
    elif place == "Abroad":
        off = 0.10
elif season == "winter":
    if place == "Bulgaria":
        is_bulgaria = True
        off = 0.08
    elif place == "Abroad":
        off = 0.15

main_string = (number_points * dancers_number) - ((number_points * dancers_number) * off)
if not is_bulgaria:
    main_string = main_string + main_string * 0.50

charity = main_string * 0.75
money_left_for_dancer = abs(charity - main_string) / dancers_number

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_left_for_dancer:.2f}")
