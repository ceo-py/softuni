main_string = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    type_command = command[0]
    if type_command == "Contains":
        letters = command[-1]
        if letters in main_string:
            print(f"{main_string} contains {letters}")
        else:
            print("Substring not found!")
    elif type_command == "Flip":
        low_or_up = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if low_or_up == "Upper":
            result = (main_string[start_index:end_index]).upper()
        else:
            result = (main_string[start_index:end_index]).lower()
        main_string = main_string[:start_index] + result + main_string[end_index:]
        print(main_string)
    elif type_command == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        main_string = main_string[:start_index] + main_string[end_index:]
        print(main_string)

    command = input()

print(f"Your activation key is: {main_string}")
