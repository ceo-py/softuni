number_colored_eggs = int(input())

red_eggs_number = 0
orange_eggs_number = 0
blue_eggs_number = 0
green_eggs_number = 0
max_eggs_number_from_color = 0
for _ in range(number_colored_eggs):
    egg_color = input()
    if egg_color == "red":
        red_eggs_number += 1
    elif egg_color == "orange":
        orange_eggs_number += 1
    elif egg_color == "blue":
        blue_eggs_number += 1
    elif egg_color == "green":
        green_eggs_number += 1

if blue_eggs_number < red_eggs_number > orange_eggs_number and red_eggs_number > green_eggs_number:
    color = "red"
    max_eggs_number_from_color = red_eggs_number

elif blue_eggs_number < orange_eggs_number > red_eggs_number and orange_eggs_number > green_eggs_number:
    color = "orange"
    max_eggs_number_from_color = orange_eggs_number

elif orange_eggs_number < blue_eggs_number > red_eggs_number and blue_eggs_number > green_eggs_number:
    color = "blue"
    max_eggs_number_from_color = blue_eggs_number

else:
    color = "green"
    max_eggs_number_from_color = green_eggs_number

print(f"Red eggs: {red_eggs_number}")
print(f"Orange eggs: {orange_eggs_number}")
print(f"Blue eggs: {blue_eggs_number}")
print(f"Green eggs: {green_eggs_number}")
print(f"Max eggs: {max_eggs_number_from_color} -> {color}")





# number_colored_eggs = int(input())
#
# eggs_info = {
#     "red": 0,
#     "orange": 0,
#     "blue": 0,
#     "green": 0
# }
#
# for _ in range(0, number_colored_eggs):
#     egg_color = input()
#     eggs_info[egg_color] += 1
#
# max_eggs = max(eggs_info, key=eggs_info.get)
#
# for color, number in eggs_info.items():
#     print(f"{color.capitalize()} eggs: {number}")
#
# print(f"Max eggs: {eggs_info[max_eggs]} -> {max_eggs}")
