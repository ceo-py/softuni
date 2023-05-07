number_one = int(input())
number_two = int(input())
number_three = int(input())


def sum_numbers(one, two):
    return one + two

def subtract(three):
    return sum_numbers(number_one, number_two) - three

print(subtract(number_three))

