command_input = input()

while command_input != "collapse":
    fiction = input()
    while fiction:
        command_input = command_input.replace(fiction, "")
        fiction = fiction[1:-1]
    if command_input:
        print(command_input)
    else:
        print("(void)")
    command_input = input()
    