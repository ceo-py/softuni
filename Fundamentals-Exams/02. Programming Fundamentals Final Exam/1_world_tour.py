main_destination = input()
command = input()


def add_stop(command_number, command_location):
    global main_destination
    how_long = int(len(main_destination))
    if how_long - 1 >= command_number:
        main_destination = main_destination[:command_number] + command_location + main_destination[command_number:]
    print(main_destination)


def remove_stop(command_number, command_location):
    global main_destination
    how_long = int(len(main_destination))
    if how_long - 1 >= command_number and how_long - 1 >= command_location:
        main_destination = main_destination[:command_number] + main_destination[1 + command_location:]
    print(main_destination)


def switch_stop(command_number, command_location):
    global main_destination
    if command_number in main_destination:
        main_destination = main_destination.replace(command_number, command_location)
    print(main_destination)


while command != "Travel":
    command = command.split(":")
    command_type = command[0]
    command_number = command[1]
    command_location = command[2]
    if command_type == "Add Stop":
        add_stop(int(command_number), command_location)
    elif command_type == "Remove Stop":
        remove_stop(int(command_number), int(command_location))
    elif command_type == "Switch":
        switch_stop(command_number, command_location)
    command = input()

print(f"Ready for world tour! Planned stops: {main_destination}")
