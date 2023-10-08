egg_colored_numbers = int(input())

red = 0
orange = 0
blue = 0
green = 0

for egg in range(egg_colored_numbers):

    color = input()

    if color == 'red':
        red += 1

    elif color == 'orange':
        orange += 1

    elif color == 'blue':
        blue += 1

    elif color == 'green':
        green += 1

max_color = 'red'
max_number = red

if orange > max_number:
    max_number = orange
    max_color = 'orange'

if blue > max_number:
    max_number = blue
    max_color = 'blue'

if green > max_number:
    max_number = green
    max_color = 'green'

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max_number} -> {max_color}')











# number_colored_eggs = int(input())
#
# red_eggs_number = 0
# orange_eggs_number = 0
# blue_eggs_number = 0
# green_eggs_number = 0
# max_eggs_number_from_color = 0
# for _ in range(number_colored_eggs):
#     egg_color = input()
#     if egg_color == "red":
#         red_eggs_number += 1
#     elif egg_color == "orange":
#         orange_eggs_number += 1
#     elif egg_color == "blue":
#         blue_eggs_number += 1
#     elif egg_color == "green":
#         green_eggs_number += 1
#
# if blue_eggs_number < red_eggs_number > orange_eggs_number and red_eggs_number > green_eggs_number:
#     color = "red"
#     max_eggs_number_from_color = red_eggs_number
#
# elif blue_eggs_number < orange_eggs_number > red_eggs_number and orange_eggs_number > green_eggs_number:
#     color = "orange"
#     max_eggs_number_from_color = orange_eggs_number
#
# elif orange_eggs_number < blue_eggs_number > red_eggs_number and blue_eggs_number > green_eggs_number:
#     color = "blue"
#     max_eggs_number_from_color = blue_eggs_number
#
# else:
#     color = "green"
#     max_eggs_number_from_color = green_eggs_number
#
# print(f"Red eggs: {red_eggs_number}")
# print(f"Orange eggs: {orange_eggs_number}")
# print(f"Blue eggs: {blue_eggs_number}")
# print(f"Green eggs: {green_eggs_number}")
# print(f"Max eggs: {max_eggs_number_from_color} -> {color}")





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




#
# red = 0
# ora = 0
# blue = 0
# green = 0
# quant = int(input())
# for i in range(quant):
#     col = input()
#     if col == 'red':
#         red += 1
#     elif col == 'orange':
#         ora += 1
#     elif col == 'blue':
#         blue += 1
#     elif col == 'green':
#         green += 1
# col_list = ['', 'red', 'orange', 'blue', 'green']
# quan_list = [0, red, ora, blue, green]
# x = max(quan_list)
# print(f'Red eggs: {red}')
# print(f'Orange eggs: {ora}')
# print(f'Blue eggs: {blue}')
# print(f'Green eggs: {green}')
# max_n = max(quan_list)
# print(f'Max eggs: {max_n} -> {col_list[quan_list.index(max_n)]}')
