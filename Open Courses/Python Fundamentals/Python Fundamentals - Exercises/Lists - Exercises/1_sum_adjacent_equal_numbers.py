main_list = [float(x) for x in input().split()]

find_numbers = True
while find_numbers:
    find_numbers = False
    for pos, num in enumerate(main_list, 1):
        if pos < len(main_list) and num == main_list[pos]:
            main_list[pos-1] = num + main_list[pos]
            del main_list[pos]
            find_numbers = True
            break

[print(f"{x:.10g}") for x in main_list]


