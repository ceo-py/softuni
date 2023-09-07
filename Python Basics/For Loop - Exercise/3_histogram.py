numbers_to_check = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(numbers_to_check):

    input_number = int(input())

    if input_number < 200:
        p1 += 1

    elif input_number < 400:
        p2 += 1

    elif input_number < 600:
        p3 += 1

    elif input_number < 800:
        p4 += 1

    elif input_number >= 800:
        p5 += 1

print(f'{p1 / numbers_to_check * 100:.2f}%')
print(f'{p2 / numbers_to_check * 100:.2f}%')
print(f'{p3 / numbers_to_check * 100:.2f}%')
print(f'{p4 / numbers_to_check * 100:.2f}%')
print(f'{p5 / numbers_to_check * 100:.2f}%')







# number_to_check = int(input())
#
# percent_under_numbers = {
#     "under 200": 0,
#     "200  - 399": 0,
#     "400 - 599": 0,
#     "600 - 799": 0,
#     "over 800": 0
# }
#
# for _ in range(0, number_to_check):
#     number = int(input())
#     if number in range(0, 200):
#         percent_under_numbers["under 200"] += 1
#     elif number in range(200, 400):
#         percent_under_numbers["200  - 399"] += 1
#     elif number in range(400, 600):
#         percent_under_numbers["400 - 599"] += 1
#     elif number in range(500, 800):
#         percent_under_numbers["600 - 799"] += 1
#     elif number >= 800:
#         percent_under_numbers["over 800"] += 1
#
# under_twohundred = (percent_under_numbers["under 200"] / number_to_check) * 100
# twohundred_fourhundred = (percent_under_numbers["200  - 399"] / number_to_check) * 100
# fourhundred_sixhundred = (percent_under_numbers["400 - 599"] / number_to_check) * 100
# sixhundred_eithhundred = (percent_under_numbers["600 - 799"] / number_to_check) * 100
# over_eithhundred = (percent_under_numbers["over 800"] / number_to_check) * 100
#
# print("{:.2f}".format(under_twohundred) + "%")
# print("{:.2f}".format(twohundred_fourhundred) + "%")
# print("{:.2f}".format(fourhundred_sixhundred) + "%")
# print("{:.2f}".format(sixhundred_eithhundred) + "%")
# print("{:.2f}".format(over_eithhundred) + "%")
