number_one = int(input())
number_two = int(input())
number_three = int(input())


def sum_numbers(one, two):
    result = one + two
    return result


def subtract(three):
    result = sum_numbers(number_one, number_two) - three
    return result


print(subtract(number_three))
