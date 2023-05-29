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
# def exchange(_, info):
#     index = info[0]
#     global main_list
#     if check_valid_index(index):
#         part_one = main_list[:index + 1]
#         part_two = main_list[index + 1:]
#         main_list = part_two + part_one
#
#
# def max_min_even_odd(max_or_min, info):
#     operation ={ "max":max, "min": min}
#     type_number = info[0]
#     if type_number == "even":
#         result = [x for x in main_list if x % 2 == 0]
#     else:
#         result = [x for x in main_list if x % 2 != 0]
#     if result:
#         ind = operation[max_or_min](result)
#         print(len(main_list) - main_list[::-1].index(ind) - 1)
#     else:
#         print("No matches")
#
#
# def first_numbers(starting_from, info):
#     number, number_type = info
#     if number > len(main_list):
#         print("Invalid count")
#         return
#     odd, even = [], []
#     for num in main_list:
#         if num % 2 != 0:
#             odd.append(num)
#         else:
#             even.append(num)
#     if starting_from == "first":
#         if number_type == "even":
#             print(even[:number])
#         elif number_type == "odd":
#             print(odd[:number])
#     elif starting_from == "last":
#         if number_type == "even":
#             print(even[-number:])
#         else:
#             print(odd[-number:])
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





# main_list = [int(x) for x in input().split()]
#
# operation = {"max": max, "min": min}
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
#
#     return [x for x in main_list if x % 2 != 0]
#
#
# def check_count(number):
#     if number > len(main_list):
#         print("Invalid count")
#         return
#
#     return True
#
#
# def exchange(_, index):
#     global main_list
#     if check_valid_index(index):
#         main_list = main_list[index + 1:] + main_list[:index + 1]
#
#
# def max_min_even_odd(max_or_min, type_number):
#     result = generate_odd_even(type_number)
#     if result:
#         ind = operation[max_or_min](result)
#         print(len(main_list) - main_list[::-1].index(ind) - 1)
#     else:
#         print("No matches")
#
#
# def first_numbers(starting_from, number, number_type):
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
#     commands[command_type](command_type, *info)
#     command = input()
#
# print(main_list)





#
# def find_max_odd(**kwargs):
#     max_odd = [el for el in list_of_integers if el % 2 != 0]
#     if max_odd:
#         found = (max(max_odd))
#         last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
#         return last_index
#     return "No matches"
#
#
# def find_max_even(**kwargs):
#     max_even = [el for el in list_of_integers if el % 2 == 0]
#     if max_even:
#         found = (max(max_even))
#         last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
#         return last_index
#     return "No matches"
#
#
# def find_min_odd(**kwargs):
#     min_odd = [el for el in list_of_integers if el % 2 != 0]
#     if min_odd:
#         found = (min(min_odd))
#         last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
#         return last_index
#     return "No matches"
#
#
# def find_min_even(**kwargs):
#     min_even = [el for el in list_of_integers if el % 2 == 0]
#     if min_even:
#         found = (min(min_even))
#         last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
#         return last_index
#     return "No matches"
#
#
# def first(**kwargs):
#     my_list = []
#     if len(list_of_integers) < count_first:
#         return "Invalid count"
#     else:
#         if even_odd == "even":
#             my_list.extend([el for el in list_of_integers if el % 2 == 0])
#             return my_list[:count_first]
#         elif even_odd == "odd":
#             my_list.extend([el for el in list_of_integers if el % 2 == 1])
#             return my_list[:count_first]
#
#
# def last(**kwargs):
#     my_list = []
#     if len(list_of_integers) < count_last:
#         return "Invalid count"
#     else:
#         if even_odd == "even":
#             my_list.extend([el for el in list_of_integers if el % 2 == 0])
#             return my_list[-count_last:]
#
#         elif even_odd == "odd":
#             my_list.extend([el for el in list_of_integers if el % 2 == 1])
#             return my_list[-count_last:]
#
#
# list_of_integers = [int(el) for el in input().split()]
# command = input()
#
# while not command == "end":
#     current_command = command.split()[0]
#     if current_command == "exchange":
#         index = int(command.split()[1])
#         if 0 <= index < len(list_of_integers):
#             list_of_integers = list_of_integers[index + 1:] + list_of_integers[:index + 1]
#
#         else:
#             print("Invalid index")
#
#     elif current_command == "max":
#         odd_or_even = command.split()[1]
#         if odd_or_even == "odd":
#             print(find_max_odd())
#
#         elif odd_or_even == "even":
#             print(find_max_even())
#
#     elif current_command == "min":
#         odd_even = command.split()[1]
#         if odd_even == "odd":
#             print(find_min_odd())
#
#         elif odd_even == "even":
#             print(find_min_even())
#
#     elif current_command == "first":
#         count_first = int(command.split()[1])
#         even_odd = command.split()[2]
#         print(first())
#
#     elif current_command == "last":
#         count_last = int(command.split()[1])
#         even_odd = command.split()[2]
#         print(last())
#
#     command = input()
# print(list_of_integers)
