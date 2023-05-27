import math

square_meters_vineyard = int(input())
square_meters_grapes = float(input())
liters_needed_wine = int(input())
workers = int(input())

vine_from_vineyard = 0.40
needed_grapes_for_liter_wine = 2.5
total_grapes = square_meters_vineyard * square_meters_grapes
wine = (vine_from_vineyard * total_grapes) / needed_grapes_for_liter_wine

if wine >= liters_needed_wine:
    left_wine = wine - liters_needed_wine
    litters_wine_per_person = left_wine / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.\n{math.ceil(left_wine)} "
          f"liters left -> {math.ceil(litters_wine_per_person)} liters per person.")
else:
    wine = abs(wine - liters_needed_wine)
    print(f"It will be a tough winter! More {math.floor(wine)} liters wine needed.")







# from math import floor
# from math import ceil
#
# vineyard_square_size = int(input())
# grapes_per_square = float(input())
# vine_lt_for_sell = int(input())
# workers = int(input())
#
# all_grape_harvest = vineyard_square_size * grapes_per_square
# total_vine = (all_grape_harvest * 0.40) / 2.5
#
# if total_vine >= vine_lt_for_sell:
#     total_vine = total_vine
#     vine_left = total_vine - vine_lt_for_sell
#     vine_per_worker = vine_left / workers
#     print(f"Good harvest this year! Total wine: {floor(total_vine)} liters."
#           f"\n{ceil(vine_left)} liters left -> {ceil(vine_per_worker)} liters per person.")
# else:
#     vine_need = abs(vine_lt_for_sell - total_vine)
#     print(f"It will be a tough winter! More {floor(vine_need)} liters wine needed.")
#
#



# import math
# x_area_sqm = int(input())
# y_greap_sqm = float(input())
# z_necessery_vine = int(input())
# workers = int(input())
# kolichestvo = (x_area_sqm*0.4*y_greap_sqm/2.5)
# if kolichestvo < z_necessery_vine:
#     q = (z_necessery_vine - kolichestvo)
#     print(f'It will be a tough winter! More {math.floor(q)} liters wine needed.')
# else:
#     print(f'Good harvest this year! Total wine: {math.floor(kolichestvo)} liters.')
#     v = (kolichestvo - z_necessery_vine)/workers
#     vino_poveche = (kolichestvo-z_necessery_vine)
#     print(f'{math.ceil(vino_poveche)} liters left -> {math.ceil(v)} liters per person.')
#
#
