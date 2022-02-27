number_check = float(input())

type_number = ""
is_type_true = False
if number_check < 1 and number_check != 0 and number_check > -1:
    type_number = "small"
    is_type_true = True

if number_check > 1_000_000 or number_check < - 1_000_000:
    type_number = "large"
    is_type_true = True

elif number_check == 0:
    print("zero")

if number_check > 0 and is_type_true:
    print(f"{type_number} positive")

if number_check < 0 and is_type_true:
    print(f"{type_number} negative")

if is_type_true == False and number_check > 0:
    print("positive")

elif is_type_true == False and number_check < 0:
    print("negative")
