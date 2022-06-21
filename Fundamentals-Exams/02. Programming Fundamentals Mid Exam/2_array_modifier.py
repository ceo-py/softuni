main_array_values = [int(n) for n in input().split()]
command = input()


def swap_command(number_one, number_two):
    global main_array_values
    main_array_values[number_one], main_array_values[number_two] = main_array_values[number_two], main_array_values[number_one]



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



# numbers = list(map(int, input().split()))
# command = input()
#
# while command != 'end':
#     command_list = command.split()
#     action = command_list[0]
#     if action == 'swap':
#         swap_one = int(command_list[1])
#         swap_two = int(command_list[2])
#         numbers[swap_one], numbers[swap_two] = numbers[swap_two], numbers[swap_one]
#     elif action == 'multiply':
#         multiplier_one = int(numbers[int(command_list[1])])
#         multiplier_two = int(numbers[int(command_list[2])])
#         multiplication = multiplier_one * multiplier_two
#         numbers[int(command_list[1])] = multiplication
#     elif command == 'decrease':
#         for pos in range(len(numbers)):
#             numbers[pos] -= 1
#     command = input()
#
# final_list = [str(i) for i in numbers]
#
# print(', '.join(final_list))
