town_name = input()
package_type = input()
vip = input()
day_stays = int(input())

price = 0
vip_discount = 1


if day_stays <= 0:
    print('Days must be positive number!')


elif town_name not in "Bansko, Borovets, Varna, Burgas" or \
        package_type not in "noEquipment, withEquipment, noBreakfast, withBreakfast":

    print('Invalid input!')

else:

    if town_name in "Bansko, Borovets":

        if package_type == 'withEquipment':
            price = 100

            if vip == 'yes':
                vip_discount = 0.90

        elif package_type == 'noEquipment':
            price = 80

            if vip == 'yes':
                vip_discount = 0.95

    elif town_name in "Varna, Burgas":

        if package_type == 'withBreakfast':
            price = 130

            if vip == 'yes':
                vip_discount = 0.88

        elif package_type == 'noBreakfast':
            price = 100

            if vip == 'yes':
                vip_discount = 0.93

    if day_stays > 7:
        day_stays -= 1

    total_price = (price * day_stays) * vip_discount
    print(f'The price is {total_price:.2f}lv! Have a nice time!')








# town_name = input()
# extras = input()
# vip_packet = input()
# days_to_stay = int(input())
#
# towns = ["Varna", "Burgas", "Bansko", "Borovets"]
# packets_type = ["withEquipment", "noEquipment", "withBreakfast", "noBreakfast"]
# total = 0
#
# if town_name not in towns or extras not in packets_type:
#     print(f"Invalid input!")
#
# elif days_to_stay < 1:
#     print(f"Days must be positive number!")
#
# else:
#     if days_to_stay > 7:
#         days_to_stay = days_to_stay - 1
#
#     if ("Bansko" == town_name or "Borovets" == town_name) and extras == "withEquipment" and vip_packet == "yes":
#         total = (days_to_stay * 100) - ((days_to_stay * 100) * 0.10)
#
#     elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "noEquipment" and vip_packet == "yes":
#         total = (days_to_stay * 80) - ((days_to_stay * 80) * 0.05)
#
#     elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "noEquipment" and vip_packet == "no":
#         total = (days_to_stay * 80)
#
#     elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "withEquipment" and vip_packet == "no":
#         total = (days_to_stay * 100)
#
#     elif ("Varna" == town_name or "Burgas" == town_name) and extras == "withBreakfast" and vip_packet == "yes":
#         total = (days_to_stay * 130) - ((days_to_stay * 130) * 0.12)
#
#     elif ("Varna" == town_name or "Burgas" == town_name) and extras == "noBreakfast" and vip_packet == "yes":
#         total = (days_to_stay * 100) - ((days_to_stay * 100) * 0.07)
#
#     elif ("Varna" == town_name or "Burgas" == town_name) and extras == "noBreakfast" and vip_packet == "no":
#         total = (days_to_stay * 100)
#
#     elif ("Varna" == town_name or "Burgas" == town_name) and extras == "withBreakfast" and vip_packet == "no":
#         total = (days_to_stay * 130)
#
#     print(f"The price is {total:.2f}lv! Have a nice time!")








# name_of_town = input()  #  ("Bansko",  "Borovets", "Varna" или "Burgas")
# type_of_package = input()  # "noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# vip_discount = input()  # "yes" or "no"
# days_of_stay = int(input())
# price_per_day = 0
# correctly_inputted_name = True
#
# towns = ["Varna", "Burgas", "Bansko", "Borovets"]
# packets_type = ["withEquipment", "noEquipment", "withBreakfast", "noBreakfast"]
# total = 0
#
# if name_of_town not in towns or type_of_package not in packets_type:
#     print(f"Invalid input!")
#
#
# elif days_of_stay < 1:
#     print("Days must be positive number!")
# else:
#     if days_of_stay > 7:
#         days_of_stay -= 1
#     if name_of_town == "Bansko" or name_of_town == "Borovets":
#         if type_of_package == "noEquipment":
#             if vip_discount == "no":
#                 price_per_day = 80
#             elif vip_discount == "yes":
#                 price_per_day = 80 * 0.95
#         elif type_of_package == "withEquipment":
#             if vip_discount == "no":
#                 price_per_day = 100
#             elif vip_discount == "yes":
#                 price_per_day = 100 * 0.90
#     elif name_of_town == "Varna" or name_of_town == "Burgas":
#         if type_of_package == "noBreakfast":
#             if vip_discount == "no":
#                 price_per_day = 100
#             elif vip_discount == "yes":
#                 price_per_day = 100 * 0.93
#         elif type_of_package == "withBreakfast":
#             if vip_discount == "no":
#                 price_per_day = 130
#             elif vip_discount == "yes":
#                 price_per_day = 130 * 0.88
#     else:
#         correctly_inputted_name = False
#
#     if correctly_inputted_name:
#         total_price = price_per_day * days_of_stay
#         print(f"The price is {total_price:.2f}lv! Have a nice time!")
#     # else:
#     #     print("Invalid input!")
#
#
