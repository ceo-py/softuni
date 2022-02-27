main_list = [int(n) for n in input().split()]

even_numbers = list()


def filter(numbers):
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


print(filter(main_list))
