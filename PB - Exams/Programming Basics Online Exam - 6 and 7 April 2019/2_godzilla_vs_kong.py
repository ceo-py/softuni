movie_budget = float(input())
person_number = int(input())
person_cloth_price = float(input())

decore = movie_budget * 0.10

if person_number > 150:
    person_cloth_price *= 0.90

total_cost = (person_cloth_price * person_number) + decore
difference = f'{abs(total_cost - movie_budget):.2f}'

if total_cost <= movie_budget:
    print('Action!')
    print(f'Wingard starts filming with {difference} leva left.')

else:
    print('Not enough money!')
    print(f'Wingard needs {difference} leva more.')





# movie_budget = float(input())
# extras = int(input())
# extras_clothing_price = float(input())
#
# decor = movie_budget * 0.10
#
# if extras > 150:
#     extras_clothing_total = (extras_clothing_price * extras) - ((extras_clothing_price * extras) * 0.10)
#
# else:
#     extras_clothing_total = extras_clothing_price * extras
#
# total_movie_cost = movie_budget - (decor + extras_clothing_total)
#
# if movie_budget > total_movie_cost and total_movie_cost >= 0:
#     print(f"Action!\nWingard starts filming with {total_movie_cost:.2f} leva left.")
#
# else:
#     print(f"Not enough money!\nWingard needs {abs(total_movie_cost):.2f} leva more.")



# film_budget = float(input())
# num_extra_people = int(input())
# price_per_person_clothing = float(input())
# decor = film_budget * 0.1
#
# if num_extra_people > 150:
#     full_price_clothing = (num_extra_people * price_per_person_clothing) * 0.9
# else:
#     full_price_clothing = num_extra_people * price_per_person_clothing
#
# total_price = full_price_clothing + decor
# rest = film_budget - total_price
# rest_printed = abs(rest)
# if total_price > film_budget:
#     print("Not enough money!")
#     print(f'Wingard needs {rest_printed:.2f} leva more.')
# elif total_price <= film_budget:
#     print("Action!")
#     print(f'Wingard starts filming with {rest_printed:.2f} leva left.')
#
