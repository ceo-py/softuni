age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print('Mr.')
if gender == 'm':
    if age < 16:
        print('Master')
if gender == 'f':
    if age >= 16:
        print('Ms.')
if gender == 'f':
    if age < 16:
        print('Miss')




# person_age = float(input())
# person_sex = input()
#
# title_check = {
#     "m under 16": "Master",
#     "m over 16": "Mr.",
#     "f under 16": "Miss",
#     "f over 16": "Ms."
# }
#
# if person_sex == "m":
#     if person_age < 16:
#         print(title_check["m under 16"])
#     else:
#         print(title_check["m over 16"])
# elif person_sex == "f":
#     if person_age < 16:
#         print(title_check["f under 16"])
#     else:
#         print(title_check["f over 16"])
