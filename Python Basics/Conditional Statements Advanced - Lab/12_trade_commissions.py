city = input()
selling_volume = float(input())
comission = 0
flag = True

if city == 'Sofia':
    if 0 <= selling_volume <= 500:
        comission = selling_volume * 0.05
    elif 500 < selling_volume <= 1000:
        comission = selling_volume * 0.07
    elif 1000 < selling_volume <= 10000:
        comission = selling_volume * 0.08
    elif 10000 < selling_volume:
        comission = selling_volume * 0.12
    else:
        flag = False
elif city == 'Varna':
    if 0 <= selling_volume <= 500:
        comission = selling_volume * 0.045
    elif 500 < selling_volume <= 1000:
        comission = selling_volume * 0.075
    elif 1000 < selling_volume <= 10000:
        comission = selling_volume * 0.10
    elif 10000 < selling_volume:
        comission = selling_volume * 0.13
    else:
        flag = False
elif city == 'Plovdiv':
    if 0 <= selling_volume <= 500:
        comission = selling_volume * 0.055
    elif 500 < selling_volume <= 1000:
        comission = selling_volume * 0.08
    elif 1000 < selling_volume <= 10000:
        comission = selling_volume * 0.12
    elif 10000 < selling_volume:
        comission = selling_volume * 0.145
    else:
        flag = False
else:
    flag = False
if flag:
    print(f'{comission:.2f}')
else:
    print('error')







#
#
# town_name = input()
# sales = float(input())
#
# commisions_town = {"Sofia": {
#     "500": 0.05,
#     "over 500 - 1000": 0.07,
#     "1000 - 10000": 0.08,
#     "over 10000": 0.12, },
#     "Varna": {
#         "500": 0.045,
#         "over 500 - 1000": 0.075,
#         "1000 - 10000": 0.10,
#         "over 10000": 0.13, },
#     "Plovdiv": {
#         "500": 0.055,
#         "over 500 - 1000": 0.08,
#         "1000 - 10000": 0.12,
#         "over 10000": 0.145, }
# }
#
# if town_name in commisions_town and sales > 0:
#     if 0 <= sales <= 500:
#         total_sales = commisions_town[town_name]["500"] * sales
#     elif 500 < sales <= 1000:
#         total_sales = commisions_town[town_name]["over 500 - 1000"] * sales
#     elif 1000 < sales <= 10000:
#         total_sales = commisions_town[town_name]["1000 - 10000"] * sales
#     elif sales > 10000:
#         total_sales = commisions_town[town_name]["over 10000"] * sales
#     print("{:.2f}".format((total_sales)))
#
# else:
#     print("error")
