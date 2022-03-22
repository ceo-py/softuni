password_to_check = input()

characters_in_range = False
letters_digits_only = False
two_digits = False
numbers_check = 0


def pass_check(check):
    global characters_in_range, letters_digits_only, two_digits, numbers_check
    if 6 <= len(check) <= 10:
        characters_in_range = True
    if check.isalnum():
        letters_digits_only = True
    for letter in check:
        if letter.isdigit():
            numbers_check += 1
        if numbers_check == 2:
            two_digits = True
            break


pass_check(password_to_check)

if all([characters_in_range, letters_digits_only, two_digits]):
    print("Password is valid")
if not characters_in_range:
    print("Password must be between 6 and 10 characters")
if not letters_digits_only:
    print("Password must consist only of letters and digits")
if not two_digits:
    print("Password must have at least 2 digits")
