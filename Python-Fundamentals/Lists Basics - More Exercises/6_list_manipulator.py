main_list = [int(n) for n in input().split()]

command_not_stop = True
list_one = list()
list_two = list()
length_main_list = len(main_list)
max_odd = 0
max_odd_index = 0
max_even = 0
max_even_index = 0
min_even = 0
min_even_index = 0
min_odd = 0
min_odd_index = 0
list_have_even_number = False
list_have_odd_number = False
list_with_even_numbers = list()
list_with_odd_numbers = list()
for n in main_list:
    n = int(n)
    if n % 2 == 0:
        list_have_even_number = True
        list_with_even_numbers.append(n)
    elif n % 2 != 0:
        list_have_odd_number = True
        list_with_odd_numbers.append(n)

while command_not_stop:
    command = input()

    if command == "end":
        command_not_stop = False
        print(main_list)
        break

    elif "exchange" in command:
        command = command.split()
        get_index = int(command[-1])
        if length_main_list <= get_index or get_index < 0:
            print("Invalid index")

        else:
            list_one = main_list[:get_index + 1]
            list_two = main_list[1 + get_index:]
            list_two.extend(list_one)
            main_list.clear()
            for n in list_two:
                main_list.append(int(n))
            list_with_even_numbers.clear()
            list_with_odd_numbers.clear()
            for n in main_list:
                n = int(n)
                if n % 2 == 0:
                    list_with_even_numbers.append(n)
                elif n % 2 != 0:
                    list_with_odd_numbers.append(n)
            list_one.clear()
            list_two.clear()

    elif "max odd" in command:
        if list_have_odd_number:
            i = 0
            max_odd = max(list_with_odd_numbers)
            max_odd_index = length_main_list - 1 - list_with_odd_numbers[::-1].index(max_odd)
            # for n in main_list:
            #     n = int(n)
            #     if n % 2 != 0 and max_odd == n:
            #         max_odd = n
            #         max_odd_index = i
            #     i += 1
            print(max_odd_index)
        else:
            print("No matches")

    elif "max even" in command:
        if list_with_even_numbers:
            i = 0
            max_even = max(list_with_even_numbers)
            max_even_index = length_main_list - 1 - list_with_even_numbers[::-1].index(max_even)
            # for n in main_list:
            #     n = int(n)
            #     if n % 2 == 0 and max_even == n:
            #         max_even = n
            #         max_even_index = i
            #     i += 1
            print(max_even_index)
        else:
            print("No matches")

    elif "min odd" in command:
        if list_have_odd_number:
            i = 0
            min_odd = min(list_with_odd_numbers)
            min_odd_index = length_main_list - 1 - list_with_odd_numbers[::-1].index(min_odd)
            # for n in main_list:
            #     n = int(n)
            #     if n % 2 != 0 and min_odd == n:
            #         min_odd = n
            #         min_odd_index = i
            #     i += 1
            print(min_odd_index)
        else:
            print("No matches")

    elif "min even" in command:
        if list_with_even_numbers:
            i = 0
            min_even = min(list_with_even_numbers)
            min_even_index = length_main_list - 1 - list_with_even_numbers[::-1].index(min_even)
            # for n in main_list:
            #     n = int(n)
            #     if n % 2 == 0 and min_even == n:
            #         min_even = n
            #         min_even_index = i
            #     i += 1
            print(min_even_index)
        else:
            print("No matches")

    elif "first" in command:
        command = command.split()
        type_number = command[2]
        number = int(command[1])
        if number >= length_main_list:
            print("Invalid count")
        else:
            if "even" in type_number:

                print(f"{list_with_even_numbers[:number]}")

            elif "odd" in type_number:

                print(f"{list_with_odd_numbers[:number]}")

    elif "last" in command:
        command = command.split()
        type_number = command[2]
        number = int(command[1])
        if number >= length_main_list:
            print("Invalid count")
        else:
            if "even" in type_number:
                print(f"{list_with_even_numbers[-number:]}")

            elif "odd" in type_number:
                print(f"{list_with_odd_numbers[-number:]}")
