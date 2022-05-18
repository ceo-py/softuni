number_one = int(input())
number_two = int(input())
first_number_gcp = []
second_number_gcp = []
for i in range(1, number_one + 1):
    if (number_one / i).is_integer():
        first_number_gcp.append(i)
for i in range(1, number_two + 1):
    if (number_two / i).is_integer():
        second_number_gcp.append(i)

# all_numbers = first_number_gcp + second_number_gcp
# seen_twice = list(set([x for x in all_numbers if all_numbers.count(x) > 1]))
seen_twice = 0
for x in sorted(first_number_gcp, reverse=True):
    if x in second_number_gcp:
        seen_twice = int(x)
        break
find_lcm = number_one == number_two
first_n = number_one
second_n = number_two
while not find_lcm:
    if number_one < number_two:
        number_one += first_n
        if number_one == number_two:
            first_n = number_one
            break
        number_two += second_n
        if number_one == number_two:
            first_n = number_one
            break
    else:
        number_two += second_n
        if number_one == number_two:
            first_n = number_one
            break
        number_one += first_n
        if number_one == number_two:
            first_n = number_one
            break

print(first_n + seen_twice)
