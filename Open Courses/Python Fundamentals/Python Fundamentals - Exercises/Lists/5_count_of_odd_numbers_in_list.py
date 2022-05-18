main_list = [int(x) for x in input().split()]


def odd_number():
    total_ = 0
    for num in main_list:
        if abs(num) % 2 != 0:
            total_ += 1
    return total_


print(odd_number())
