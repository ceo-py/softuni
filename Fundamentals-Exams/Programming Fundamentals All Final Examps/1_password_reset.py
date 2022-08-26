main_string = input()
command = input()


def take_odd_char(main_string):

    return "".join(main_string[i] for i in range(len(main_string)) if i % 2 != 0)


def cut_string(index, length, main_string):
    return main_string[:index] + main_string[index + length:]


def substitute(substring, substitute, main_string):
    return main_string.replace(substring, substitute)


while command != "Done":
    nothing_to_replace = False
    if "TakeOdd" in command:
        main_string = take_odd_char(main_string)
    else:
        _, index_or_substring, length_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
        if "Cut" in command:
            main_string = cut_string(index_or_substring, length_or_substitute, main_string)
        elif "Substitute" in command:
            if index_or_substring in main_string:
                main_string = substitute(index_or_substring, length_or_substitute, main_string)
            else:
                print("Nothing to replace!")
                nothing_to_replace = True
    if not nothing_to_replace:
        print(main_string)

    command = input()

print(f"Your password is: {main_string}")