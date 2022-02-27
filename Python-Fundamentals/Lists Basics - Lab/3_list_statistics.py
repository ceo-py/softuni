number_range = int(input())

list_plus = list()
list_minus = list()
minus_count = 0
plus_count = 0

for _ in range(number_range):
    number = int(input())

    if number >= 0:
        list_plus.append(number)
        plus_count += 1

    else:
        list_minus.append(number)
        minus_count += number

print(f"{list_plus}\n{list_minus}")
print(f"Count of positives: {plus_count}")
print(f"Sum of negatives: {minus_count}")
