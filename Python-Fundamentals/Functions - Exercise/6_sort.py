main_list = [int(n) for n in input().split()]
sort_list = list()


def sorted(numbers):
    numbers.sort()
    for n in numbers:
        sort_list.append(n)
    return sort_list


print(sorted(main_list))
