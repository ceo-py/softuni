main_data = [int(x) for x in input().split()]


def exchange_list(index_):
    global main_data
    if len(main_data) > index_ >= 0:
        side_a = main_data[:index_ + 1]
        side_b = main_data[index_ + 1:]
        main_data.clear()
        main_data = side_b + side_a
    else:
        print("Invalid index")


def max_number(odd_or_even):
    max_num = min(main_data)
    pos_num = 0
    find_number = False
    for pos, num in enumerate(main_data):
        if all([odd_or_even == "even", num % 2 == 0, num >= max_num]):
            max_num = num
            pos_num = pos
            find_number = True
        elif all([odd_or_even == "odd", num % 2 != 0, num >= max_num]):
            max_num = num
            pos_num = pos
            find_number = True
    if find_number:
        return pos_num
    else:
        return "No matches"


def min_number(odd_or_even):
    min_number = max(main_data)
    pos_num = 0
    find_number = False
    for pos, num in enumerate(main_data):
        if all([odd_or_even == "even", num % 2 == 0, num <= min_number]):
            min_number = num
            pos_num = pos
            find_number = True
        elif all([odd_or_even == "odd", num % 2 != 0, num <= min_number]):
            min_number = num
            pos_num = pos
            find_number = True
    if find_number:
        return pos_num
    else:
        return "No matches"


def first_count(number, odd_or_even):
    count_show = []
    if number <= len(main_data):
        for num in main_data:
            if all([odd_or_even == "even", num % 2 == 0]):
                count_show.append(num)
            elif all([odd_or_even == "odd", num % 2 != 0]):
                count_show.append(num)
        return count_show[:number]
    else:
        return "Invalid count"


def last_count(number, odd_or_even):
    count_show = []
    if number <= len(main_data):
        for num in main_data:
            if all([odd_or_even == "even", num % 2 == 0]):
                count_show.append(num)
            elif all([odd_or_even == "odd", num % 2 != 0]):
                count_show.append(num)
        return count_show[-number:]
    else:
        return "Invalid count"


command_type = input()

while command_type != "end":
    command_type, *info = command_type.split()
    if command_type == "max":
        print(max_number(info[0]))
    elif command_type == "min":
        print(min_number(info[0]))
    elif command_type == "first":
        print(first_count(int(info[0]), info[1]))
    elif command_type == "last":
        print(last_count(int(info[0]), info[1]))
    elif command_type == "exchange":
        exchange_list(int(info[0]))

    command_type = input()

print(main_data)
