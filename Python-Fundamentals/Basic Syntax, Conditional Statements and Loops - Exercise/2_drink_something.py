drinking_age = int(input())

age_info = {
    "drink toddy": 14,
    "drink coke": 18,
    "drink beer": 21,
    "drink whisky": 100
}
for drinks, age in age_info.items():
    if drinking_age <= age:
        print(drinks)
        break



#
# drinking_age = int(input())
#
# if drinking_age <= 14:
#     print("drink toddy")
#
# elif drinking_age <= 18:
#     print("drink coke")
#
# elif drinking_age <= 21:
#     print("drink beer")
#
# else:
#     print("drink whisky")
