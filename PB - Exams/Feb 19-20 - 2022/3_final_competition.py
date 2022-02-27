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

result = (number_points * dancers_number) - ((number_points * dancers_number) * off)
if not is_bulgaria:
    result = result + result * 0.50

charity = result * 0.75
money_left_for_dancer = abs(charity - result) / dancers_number

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_left_for_dancer:.2f}")
