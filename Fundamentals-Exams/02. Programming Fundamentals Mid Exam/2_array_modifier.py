main_array_values = [int(n) for n in input().split()]
command = input()


def swap_command(number_one, number_two):
    global main_array_values
    first_element = main_array_values[number_one]
    second_element = main_array_values[number_two]
    main_array_values[number_one] = second_element
    main_array_values[number_two] = first_element


def multiply_command(number_one, number_two):
    global main_array_values
    result_multiply = main_array_values[number_one] * main_array_values[number_two]
    main_array_values[number_one] = result_multiply


def decrease_command():
    global main_array_values
    main_array_values = [x - 1 for x in main_array_values[:]]


while command != "end":
    command = command.split()
    command_name = command[0]
    if command_name == "decrease":
        decrease_command()
    else:
        number_one = int(command[1])
        number_two = int(command[2])

    if command_name == "swap":
        swap_command(number_one, number_two)

    elif command_name == "multiply":
        multiply_command(number_one, number_two)
    command = input()

print(*main_array_values, sep=", ")
