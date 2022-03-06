main_string = input()

command = input()


def take_odd():
    global main_string
    copy_main_string = main_string[:]
    main_string = ""
    for index, char in enumerate(copy_main_string):
        if index % 2 != 0:
            main_string += char
    print(main_string)


def cut_string(index, lenght_string):
    global main_string
    main_string = main_string[:index] + "" + main_string[index + lenght_string:]
    print(main_string)


def substitute_string(substring, substitute):
    global main_string
    if substring in main_string:
        main_string = main_string.replace(substring, substitute)
        print(main_string)
    else:
        print("Nothing to replace!")


while command != "Done":
    command = command.split()
    type_command = command[0]
    if type_command == "TakeOdd":
        take_odd()
    elif type_command == "Cut":
        cut_string(int(command[1]), int(command[-1]))
    elif type_command == "Substitute":
        substitute_string(command[1], command[-1])
    command = input()

print(f"Your password is: {main_string}")
