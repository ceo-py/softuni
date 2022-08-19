from collections import deque

mixed_colors = deque(input().split())

colors = ["orange", "purple", "green", "red", "yellow", "blue"]

final_colors = []
sec_colors_temp = deque()


def add_find_color(start_color, end_color):
    final_colors.append(f"{start_color}{end_color}")


def check_for_secondary_color(start_color, end_color=""):
    if start_color + end_color in "orange purple green":
        sec_colors_temp.append(start_color + end_color)
        return True
    elif end_color + start_color in "orange purple green":
        sec_colors_temp.append(end_color + start_color)
        return True


def adding_secondary_color(start_color, end_color):
    guessed_color = start_color + end_color
    for _ in range(2):
        if guessed_color == "orange" and "red" in final_colors and "yellow" in final_colors:
            final_colors.append(guessed_color)
            # sec_colors_temp.remove(guessed_color)
            break
        elif guessed_color == "purple" and "red" in final_colors and "blue" in final_colors:
            final_colors.append(guessed_color)
            # sec_colors_temp.remove(guessed_color)
            break
        elif guessed_color == "green" and "yellow" in final_colors and "blue" in final_colors:
            final_colors.append(guessed_color)
            # sec_colors_temp.remove(guessed_color)
            break
        guessed_color = end_color + start_color


while mixed_colors:
    if len(mixed_colors) >= 2:
        start_color = mixed_colors.popleft()
        end_color = mixed_colors.pop()

        if check_for_secondary_color(start_color, end_color):
            adding_secondary_color(start_color, end_color)

        elif f"{start_color}{end_color}" in colors:
            final_colors.append(f"{start_color}{end_color}")

        elif f"{end_color}{start_color}" in colors:
            add_find_color(end_color, start_color)

        else:
            middle_of_colors = len(mixed_colors) // 2
            start_color = start_color[:-1]
            end_color = end_color[:-1]
            if start_color:
                mixed_colors.insert(middle_of_colors, start_color)
            if end_color:
                mixed_colors.insert(middle_of_colors, end_color)

    elif len(mixed_colors) == 1:
        guessed_color = mixed_colors.popleft()
        if guessed_color in "orange purple green":
            if guessed_color == "orange" and "red" in final_colors and "yellow" in final_colors:
                final_colors.append(guessed_color)
            elif guessed_color == "purple" and "red" in final_colors and "blue" in final_colors:
                final_colors.append(guessed_color)
            elif guessed_color == "green" and "yellow" in final_colors and "blue" in final_colors:
                final_colors.append(guessed_color)
        elif guessed_color in colors:
            final_colors.append(guessed_color)

while sec_colors_temp:
    guessed_color = sec_colors_temp.popleft()
    adding_secondary_color(guessed_color, "")

print(final_colors)
