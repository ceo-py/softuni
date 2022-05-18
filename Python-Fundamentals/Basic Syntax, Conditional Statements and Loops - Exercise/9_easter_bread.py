budget = float(input())
price_of_kg_flour = float(input())

eggs_pack = price_of_kg_flour * 0.75
milk_one_l = (price_of_kg_flour * 1.25) / 4
colored_eggs = 0
for number_breads in range(1, int(budget) + 1):
    if eggs_pack + milk_one_l + price_of_kg_flour <= budget:
        budget -= (eggs_pack + milk_one_l + price_of_kg_flour)
        colored_eggs += 3
        if number_breads % 3 == 0:
            colored_eggs -= (number_breads - 2)
    else:
        print(
            f"You made {number_breads - 1} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
