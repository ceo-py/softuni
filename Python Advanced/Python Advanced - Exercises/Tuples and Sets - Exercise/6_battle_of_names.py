number_of_names = int(input())

odd_numbers = set()
even_numbers = set()

for row in range(1, number_of_names + 1):
    name = input()
    current_name_score = 0
    for ltr in name:
        current_name_score += ord(ltr)
    number_to_add = int(current_name_score/row)
    if number_to_add % 2 != 0:
        odd_numbers.add(number_to_add)
    else:
        even_numbers.add(number_to_add)

if sum(odd_numbers) < sum(even_numbers):
    print(*even_numbers.symmetric_difference(odd_numbers), sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*odd_numbers.union(even_numbers), sep=", ")