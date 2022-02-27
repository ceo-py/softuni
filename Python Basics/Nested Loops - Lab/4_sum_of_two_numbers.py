number = int(input())
number_end = int(input())
magic_number = int(input())

combinations_count = 0
stop = 0

for x1 in range(number, number_end + 1):
    for x2 in range(number, number_end + 1):
        if x1 + x2 == magic_number:
            combinations_count += 1
            total = x1 + x2
            stop += 1
            print(f"Combination N:{combinations_count} ({x1} + {x2} = {total})")
            break
        else:
            combinations_count += 1
    if x1 + x2 == magic_number:
        total = x1 + x2
        stop += 1
        break

if stop != 2:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
