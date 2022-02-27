number = int(input())


def loading_bar(num):
    num_range = int(num / 10)
    target = 10
    if target == num_range:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{num}% " + "[" + num_range * "%" + (target - num_range) * "." + "]\n" + "Still loading..."


print(loading_bar(number))
