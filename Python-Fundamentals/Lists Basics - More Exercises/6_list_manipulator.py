def find_max_odd(**kwargs):
    max_odd = [el for el in list_of_integers if el % 2 != 0]
    if max_odd:
        found = (max(max_odd))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_max_even(**kwargs):
    max_even = [el for el in list_of_integers if el % 2 == 0]
    if max_even:
        found = (max(max_even))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_min_odd(**kwargs):
    min_odd = [el for el in list_of_integers if el % 2 != 0]
    if min_odd:
        found = (min(min_odd))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def find_min_even(**kwargs):
    min_even = [el for el in list_of_integers if el % 2 == 0]
    if min_even:
        found = (min(min_even))
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(found)
        return last_index
    return "No matches"


def first(**kwargs):
    my_list = []
    if len(list_of_integers) < count_first:
        return "Invalid count"
    else:
        if even_odd == "even":
            my_list.extend([el for el in list_of_integers if el % 2 == 0])
            return my_list[:count_first]
        elif even_odd == "odd":
            my_list.extend([el for el in list_of_integers if el % 2 == 1])
            return my_list[:count_first]


def last(**kwargs):
    my_list = []
    if len(list_of_integers) < count_last:
        return "Invalid count"
    else:
        if even_odd == "even":
            my_list.extend([el for el in list_of_integers if el % 2 == 0])
            return my_list[-count_last:]

        elif even_odd == "odd":
            my_list.extend([el for el in list_of_integers if el % 2 == 1])
            return my_list[-count_last:]


list_of_integers = [int(el) for el in input().split()]
command = input()

while not command == "end":
    current_command = command.split()[0]
    if current_command == "exchange":
        index = int(command.split()[1])
        if 0 <= index < len(list_of_integers):
            list_of_integers = list_of_integers[index + 1:] + list_of_integers[:index + 1]

        else:
            print("Invalid index")

    elif current_command == "max":
        odd_or_even = command.split()[1]
        if odd_or_even == "odd":
            print(find_max_odd())

        elif odd_or_even == "even":
            print(find_max_even())

    elif current_command == "min":
        odd_even = command.split()[1]
        if odd_even == "odd":
            print(find_min_odd())

        elif odd_even == "even":
            print(find_min_even())

    elif current_command == "first":
        count_first = int(command.split()[1])
        even_odd = command.split()[2]
        print(first())

    elif current_command == "last":
        count_last = int(command.split()[1])
        even_odd = command.split()[2]
        print(last())

    command = input()
print(list_of_integers)