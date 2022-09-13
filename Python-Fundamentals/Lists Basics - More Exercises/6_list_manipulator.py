numbers = [int(i) for i in input().split()]
command = input().split()

while command[0] != "end":
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[0:int(command[1])])
            else:
                print(odd[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[-int(command[1]):])
            else:
                print(odd[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)













# main_list = [int(x) for x in input().split()]
#
#
# def check_valid_index(index):
#     if 0 <= index < len(main_list):
#         return True
#     print("Invalid index")
#
#
# def generate_odd_even(type_number):
#     if type_number == "even":
#         return [x for x in main_list if x % 2 == 0]
#     else:
#         return [x for x in main_list if x % 2 != 0]
#
#
# def check_count(number):
#     if number > len(main_list):
#         print("Invalid count")
#         return
#     return True
#
#
# def exchange(_, info):
#     global main_list
#     index = info[0]
#     if check_valid_index(index):
#         main_list = main_list[index + 1:] + main_list[:index + 1]
#
#
# def max_min_even_odd(max_or_min, info):
#     type_number, operation = info[0], {"max": max, "min": min}
#     result = generate_odd_even(type_number)
#     if result:
#         ind = operation[max_or_min](result)
#         print(len(main_list) - main_list[::-1].index(ind) - 1)
#     else:
#         print("No matches")
#
#
# def first_numbers(starting_from, info):
#     number, number_type = info
#     if check_count(number):
#         p_result = {"first": generate_odd_even(number_type)[:number],
#                     "last": generate_odd_even(number_type)[-number:]}
#         print(p_result[starting_from])
#
#
# commands = {
#     "max": max_min_even_odd,
#     "min": max_min_even_odd,
#     "first": first_numbers,
#     "last": first_numbers,
#     "exchange": exchange
#
# }
#
# command = input()
#
# while command != "end":
#     command_type, *info = [x if x.isalpha() else int(x) for x in command.split()]
#     commands[command_type](command_type, info)
#     command = input()
#
# print(main_list)
