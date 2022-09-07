from collections import deque


def best_list_pureness(*args):
    list_rotate, number_of_rotations = deque(args[0]), args[1]
    list_len = len(list_rotate)

    def sum_pureness(list_data):
        total = 0
        for i in range(list_len):
            total += list_data[i] * i
        return total

    result = {
        "0": sum_pureness(list_rotate)
    }
    for rotation in range(1, number_of_rotations + 1):
        list_rotate.rotate(1)
        result[rotation] = result.get(rotation, sum_pureness(list_rotate))
    best_rotation = max(result, key=result.get)
    return f"Best pureness {result[best_rotation]} after {best_rotation} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
