detergent_washing_dishes = int(input())

bottle = 750
one_dish = 5
one_pot = 15

total_preparation = detergent_washing_dishes * bottle
dishes_count = 0
pot_count = 0
total_dishes_wash = 0
total_pot_wash = 0
washed_dishes = 0
washed_pots = 0
while True:
    if total_preparation < 0:
        print(f"Not enough detergent, {abs(total_preparation)} ml. more necessary!")
        break
    items_insert_in_dish_washer = input()
    if items_insert_in_dish_washer == "End":
        print(f"Detergent was enough!\n{total_dishes_wash} dishes and {total_pot_wash} "
              f"pots were washed.\nLeftover detergent {total_preparation} ml.")
        break
    items_insert_in_dish_washer = int(items_insert_in_dish_washer)
    dishes_count += 1
    if dishes_count <= 2:
        total_dishes_wash += items_insert_in_dish_washer
        washed_dishes = total_preparation - (items_insert_in_dish_washer * one_dish)
        total_preparation = washed_dishes
        if washed_dishes > total_preparation:
            total = total_preparation - washed_dishes
            print(f"Not enough detergent, {total} ml. more necessary!")
    else:
        total_pot_wash += items_insert_in_dish_washer
        pot_count += items_insert_in_dish_washer
        washed_pots = total_preparation - (items_insert_in_dish_washer * one_pot)
        total_preparation = washed_pots
        dishes_count = 0
