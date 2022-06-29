price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()
left_side = 0
right_side = 0


def cheap():
    global left_side, right_side
    left_side = min(price_ratings[:entry_point])
    right_side = min(price_ratings[entry_point:])


def expensive():
    global left_side, right_side
    left_side = sum(price_ratings[:entry_point])
    right_side = sum(price_ratings[entry_point:])


if type_of_items == "cheap":
    cheap()
else:
    expensive()

if left_side >= right_side:
    print(f"Left - {left_side}")
else:
    print(f"Right - {right_side}")

