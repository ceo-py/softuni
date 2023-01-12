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




# budget = float(input())
# flour_price = float(input())
# eggs_price = flour_price * 0.75
# milk_price = (flour_price * 1.25) / 4
# loaf_price = flour_price + eggs_price + milk_price
#
# colored_eggs = 0
# bread_loaves = 0
#
# while True:
#
#     if budget <= loaf_price:
#         print(f"You made {bread_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
#         break
#
#     budget -= loaf_price
#     bread_loaves += 1
#     colored_eggs += 3
#
#     if bread_loaves % 3 == 0:
#         colored_eggs -= bread_loaves - 2