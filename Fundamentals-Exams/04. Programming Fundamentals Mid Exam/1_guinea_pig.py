food_kgs = float(input())*1000
hay_kgs = float(input())*1000
cover_kgs = float(input())*1000
guinea_weight_kgs = float(input())*1000

cover = guinea_weight_kgs / 3
feed_eaten = 0

for day in range(1, 31):
    feed_eaten += 300
    food_kgs -= 300
    if day % 2 == 0:
        hay = food_kgs * 0.05
        hay_kgs -= hay
        feed_eaten += hay

    if day % 3 == 0:
        cover_kgs -= cover

if food_kgs > 0 and hay_kgs > 0 and cover_kgs > 0:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food_kgs/1000:.2f}, "
          f"Hay: {hay_kgs/1000:.2f}, "
          f"Cover: {cover_kgs/1000:.2f}.")

else:
    print("Merry must go to the pet store!")







#
#
#
#
#
# food_kg, hay_kg, cover_kg, weight_kg = float(input()), float(input()), float(input()), float(input())
#
# convert_rate = 1_000
# food_kg *= convert_rate
# hay_kg *= convert_rate
# cover_kg *= convert_rate
# weight_kg *= convert_rate / 3
# enough_food = True
# for day in range(1, 31):
#     food_kg += - 300
#     if day % 2 == 0:
#         hay_kg += - food_kg * 0.05
#     if day % 3 == 0:
#         cover_kg += -weight_kg
#     if all([food_kg > 0.00, hay_kg > 0.00, cover_kg > 0.00]):
#         continue
#     else:
#         enough_food = False
#         break
#
# if enough_food:
#     print(f"Everything is fine! Puppy is happy! Food: {(food_kg/convert_rate):.2f}, "
#           f"Hay: {(hay_kg/convert_rate):.2f}, Cover: {(cover_kg/convert_rate):.2f}.")
# else:
#     print("Merry must go to the pet store!")
