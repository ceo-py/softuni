first_set_sep, second_set_sep = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for num in range(first_set_sep):
    first_set.add(input())

for num in range(second_set_sep):
    second_set.add(input())

print("\n".join(first_set.intersection(second_set)))






#
#
# first_set_sep, second_set_sep = [int(num) for num in input().split()]
#
# all_numbers = [input() for _ in range(first_set_sep+second_set_sep)]
# print("\n".join(list(set(all_numbers[:first_set_sep]) & set(all_numbers[first_set_sep:]))))
