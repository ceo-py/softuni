list_with_numbers = [int(input()) for _ in range(4)]


def first_alone():
    if list_with_numbers[0] == sum(list_with_numbers[1:]):
        return "Yes", list_with_numbers[0]
    return "No"


def first_and_second():
    if list_with_numbers[0] + list_with_numbers[1] == sum(list_with_numbers[2:]):
        return "Yes", list_with_numbers[0] + list_with_numbers[1]
    return "No"


def first_and_third():
    if list_with_numbers[0] + list_with_numbers[2] == list_with_numbers[1] + list_with_numbers[3]:
        return "Yes", list_with_numbers[2] + list_with_numbers[0]
    return "No"


def first_and_four():
    if list_with_numbers[0] + list_with_numbers[3] == list_with_numbers[1] + list_with_numbers[2]:
        return "Yes", list_with_numbers[3] + list_with_numbers[0]
    return "No"


def add_first_to_end():
    list_with_numbers.append(list_with_numbers.pop(0))


for test in range(4):
    if "Yes" in first_alone():
        status, number = first_alone()
        print(f"{status}\n{number}")
        break

    elif "Yes" in first_and_second():
        status, number = first_and_second()
        print(f"{status}\n{number}")
        break

    elif "Yes" in first_and_third():
        status, number = first_and_third()
        print(f"{status}\n{number}")
        break

    elif "Yes" in first_and_four():
        status, number = first_and_four()
        print(f"{status}\n{number}")
        break

    add_first_to_end()


else:
    print("No")
