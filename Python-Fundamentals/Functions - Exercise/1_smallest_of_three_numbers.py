numbers = list()

for _ in range(3):
    num = int(input())
    numbers.append(num)


def find_smallest_number(list_of_numbers):
    result = min(list_of_numbers)
    return result


print(find_smallest_number(numbers))
