number_check = float(input())

how_big = {
    "small": all([number_check < 1, number_check != 0, number_check > -1]),
    "large": any([number_check > 1_000_000, number_check < - 1_000_000]),
    "zero": number_check == 0,
    "positive": number_check > 0,
    "negative": number_check < 0
}

for items in how_big.items():
    if items[1]:
        print(items[0], end=" ")



# number_check = float(input())
#
# type_number = ""
# is_type_true = False
# if number_check < 1 and number_check != 0 and number_check > -1:
#     type_number = "small"
#     is_type_true = True
#
# if number_check > 1_000_000 or number_check < - 1_000_000:
#     type_number = "large"
#     is_type_true = True
#
# elif number_check == 0:
#     print("zero")
#
# if number_check > 0 and is_type_true:
#     print(f"{type_number} positive")
#
# if number_check < 0 and is_type_true:
#     print(f"{type_number} negative")
#
# if is_type_true == False and number_check > 0:
#     print("positive")
#
# elif is_type_true == False and number_check < 0:
#     print("negative")
