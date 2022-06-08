first_set_sep, second_set_sep = [int(num) for num in input().split()]

all_numbers = [input() for _ in range(first_set_sep+second_set_sep)]
print("\n".join(list(set(all_numbers[:first_set_sep]) & set(all_numbers[first_set_sep:]))))
