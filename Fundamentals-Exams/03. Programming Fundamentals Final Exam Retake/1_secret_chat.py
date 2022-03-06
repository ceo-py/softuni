main_msg = input()
command = input()


def change_msg(substring, replacement):
    global main_msg
    main_msg = main_msg.replace(substring, replacement)
    print(main_msg)


def inset_space(index):
    global main_msg
    main_msg = main_msg[:index] + " " + main_msg[index:]
    print(main_msg)


def reverse(substring):
    global main_msg
    if substring in main_msg:
        word_find = main_msg.find(substring)
        main_msg = main_msg[:word_find] + "" + main_msg[word_find + (len(substring)):]
        main_msg += substring[::-1]
        print(main_msg)
    else:
        print("error")


while command != "Reveal":
    command = command.split(":|:")
    command_type = command[0]
    if command_type == "ChangeAll":
        substring = command[1]
        replacement = command[-1]
        change_msg(substring, replacement)

    elif command_type == "Reverse":
        substring = command[1]
        reverse(substring)

    elif command_type == "InsertSpace":
        index_for_insert = int(command[-1])
        inset_space(index_for_insert)

    command = input()

print(f"You have a new text message: {main_msg}")
