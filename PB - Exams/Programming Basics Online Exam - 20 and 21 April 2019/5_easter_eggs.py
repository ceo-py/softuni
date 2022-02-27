number_colored_eggs = int(input())

eggs_info = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0
}

for _ in range(0, number_colored_eggs):
    egg_color = input()
    eggs_info[egg_color] += 1

max_eggs = max(eggs_info, key=eggs_info.get)

for color, number in eggs_info.items():
    print(f"{color.capitalize()} eggs: {number}")

print(f"Max eggs: {eggs_info[max_eggs]} -> {max_eggs}")