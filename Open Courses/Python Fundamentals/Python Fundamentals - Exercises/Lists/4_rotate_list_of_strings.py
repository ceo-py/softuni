main_list = [x for x in input().split()]


def rotate_list():
    return main_list.insert(0, main_list.pop())


rotate_list()
print(*main_list)
