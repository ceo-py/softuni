password_type = input()


def check_password(check):
    how_long = len(check)
    total_numbers = 0
    range_numbers = False
    digits_check = False

    if 6 <= how_long <= 10:
        range_numbers = True
    else:
        print(f"Password must be between 6 and 10 characters")

    for n in check:
        if n.isdigit() or n.isalpha():
            total_numbers += 1
        if n.isdigit():
            digits_check = True

    if check.isalnum() is False:
        print("Password must consist only of letters and digits")

    if digits_check == False:
        print(f"Password must have at least 2 digits")

    if  check.isalnum() and total_numbers == how_long and range_numbers:
        print("Password is valid")


check_password(password_type)
