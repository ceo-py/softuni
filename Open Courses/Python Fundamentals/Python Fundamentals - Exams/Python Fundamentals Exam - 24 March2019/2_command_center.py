main_list = [int(x) for x in input().split()]
commands_received = input()


total_count = 0


def swap(num_one, num_two):
    num_one = int(num_one)
    how_big = len(main_list)
    if all([num_one in range(how_big), num_two in range(how_big)]):
        main_list[num_one], main_list[num_two] = main_list[num_two], main_list[num_one]
    return main_list


def enumerate_list(*trash):
    return list(enumerate(main_list))


def get_divisible(_, num):
    return [x for x in main_list if x % num == 0]


command_list = [swap, enumerate_list, get_divisible, max, min]

while commands_received != "end":
    command = commands_received.split()
    for function in command_list:
        if function.__name__ == command[0]:
            if len(command) == 1:
                result_ = function(main_list)
            else:
                result_ = function(command[1], int(command[-1]))
            print(result_)
            total_count += 1
            break

    commands_received = input()

print(total_count)


# main_list = [int(x) for x in input().split()]
#
# commands_received = input()
# total_count = 0
#
#
# def swap_command(num_one, num_two):
#     how_big = len(main_list)
#     if num_one in range(how_big) and num_two in range(how_big):
#         one = main_list[num_one]
#         second = main_list[num_two]
#         main_list[num_one] = second
#         main_list[num_two] = one
#     print(main_list)
#
#
# def enumerate_list():
#     how_big = len(main_list)
#     print("[", end="")
#     for pos, n in enumerate(main_list):
#         if pos + 1 < how_big:
#             print(f"({pos}, {n})", end=", ")
#         else:
#             print(f"({pos}, {n})", end="")
#     print("]")
#
#
# def devisible(num):
#     show_list = []
#     for n in main_list:
#         if n % num == 0:
#             show_list.append(n)
#     print(show_list)
#
#
# while commands_received != "end":
#     command_type = commands_received.split()
#     if "swap" == command_type[0]:
#         total_count += 1
#         swap_command(int(command_type[1]), int(command_type[-1]))
#     elif "enumerate_list" == command_type[0]:
#         total_count += 1
#         enumerate_list()
#     elif "max" == command_type[0]:
#         total_count += 1
#         print(max(main_list))
#     elif "min" == command_type[0]:
#         total_count += 1
#         print(min(main_list))
#     elif "get_divisible" == command_type[0] and "by" == command_type[1]:
#         total_count += 1
#         devisible(int(command_type[-1]))
#
#     commands_received = input()
#
# print(total_count)
