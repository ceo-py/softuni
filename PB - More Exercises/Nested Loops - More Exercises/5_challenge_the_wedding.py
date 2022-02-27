numbers_man = int(input())
numbers_woman = int(input())
total_tables = int(input())

tables_left = 0

for i in range(1, numbers_man + 1):
    for o in range(1, numbers_woman + 1):
        if total_tables == tables_left:
            break
        else:
            print(f"({i} <-> {o})", end=" ")
            tables_left += +1