main_string = input()

commands_string = input()

while commands_string != "end":
    if "Delete" in commands_string:
        _, star_index, end_index = commands_string.split()
        main_string = main_string[:int(star_index)] + main_string[int(end_index) + 1:]
    elif "Insert" in commands_string:
        _, star_index, word = commands_string.split()
        star_index = int(star_index)
        if len(main_string) == star_index:
            main_string += word
        else:
            main_string = word + main_string[star_index:]
    elif "Left" in commands_string:
        pass
    commands_string = input()

print(main_string)