from math import ceil

cozunak_number = int(input())
sugar_max_spend = 0
flour_max_spend = 0
sugar_total = 0
flour_total = 0

for cozunak in range(cozunak_number):
    sugar_spend = int(input())
    flour_spend = int(input())
    sugar_total += sugar_spend
    flour_total += flour_spend

    if sugar_spend > sugar_max_spend:
        sugar_max_spend = sugar_spend

    if flour_spend > flour_max_spend:
        flour_max_spend = flour_spend

sugar_used = ceil(sugar_total / 950)
flour_used = ceil(flour_total / 750)

print(f'Sugar: {sugar_used}')
print(f'Flour: {flour_used}')
print(f'Max used flour is {flour_max_spend} grams, max used sugar is {sugar_max_spend} grams.')







# import math
#
# easter_cakes_numbers = int(input())
#
# sugar_needed = 0
# flour_needed = 0
# sugar_max_used = 0
# flour_max_used = 0
#
# for _ in range(0, easter_cakes_numbers):
#     sugar_gr = int(input())
#     flour_gr = int(input())
#     sugar_needed += sugar_gr
#     flour_needed += flour_gr
#     if sugar_gr > sugar_max_used:
#         sugar_max_used = sugar_gr
#
#     if flour_gr > flour_max_used:
#         flour_max_used = flour_gr
#
# sugar_packets = math.ceil(sugar_needed / 950)
# flour_packets = math.ceil(flour_needed / 750)
#
# print(f"Sugar: {sugar_packets}\nFlour: {flour_packets}")
# print(f"Max used flour is {flour_max_used} grams, max used sugar is {sugar_max_used} grams.")
