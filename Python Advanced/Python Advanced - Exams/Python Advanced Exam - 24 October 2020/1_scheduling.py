jobs = [int(x) for x in input().split(", ")]
index_to_find = int(input())
clock_cycles = 0


def change_number(index):
    jobs[index] = "x"


for num in sorted(jobs[:]):
    found_index = jobs.index(num)
    clock_cycles += jobs[found_index]
    change_number(found_index)
    if found_index == index_to_find:
        break

print(clock_cycles)