main_list = [float(n) for n in input().split()]


def round_numbers(numbers):
    result = [round(num) for num in numbers]
    return result


print(round_numbers(main_list))
