from collections import deque

cups_capacity = deque(int(x) for x in input().split())
filled_bottles = [int(x) for x in input().split()]

wasted_litters_of_water = 0

while cups_capacity and filled_bottles:
    bottle = filled_bottles.pop()
    cups_capacity[0] -= bottle
    if cups_capacity[0] <= 0:
        wasted_litters_of_water += abs(cups_capacity[0])
        del cups_capacity[0]

if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
else:
    print(f"Bottles: {' '.join(str(x) for x in filled_bottles)}")

print(f"Wasted litters of water: {wasted_litters_of_water}")
