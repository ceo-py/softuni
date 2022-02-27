quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
spirit_points = 0
total_budget = 0
if days % 10 == 0:
    spirit_points = - 30

for day in range(1, days + 1):


    if day % 2 == 0:
        total_budget += (ornament_set * quantity)
        spirit_points += 5

    if day % 3 == 0:
        total_budget += (tree_skirt * quantity) + (tree_garlands * quantity)
        spirit_points += 13

    if day % 5 == 0:
        total_budget += tree_lights * quantity
        spirit_points += 17
        if day % 3 == 0:
            spirit_points += 30

    if day % 10 == 0:
        total_budget += tree_skirt + tree_garlands + tree_lights
        spirit_points += - 20
        quantity += 2

    if day > days:
        break


print(f"Total cost: {total_budget}")
print(f"Total spirit: {spirit_points}")