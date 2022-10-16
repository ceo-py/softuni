errors = []


def password_validation(password):
    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum(1 for x in password if x.isdigit()) < 2:
        errors.append("Password must have at least 2 digits")


current_password = input()
password_validation(current_password)
if errors:
    [print(show) for show in errors]
else:
    print("Password is valid")








#
# errors = {
#     "leng": "Password must be between 6 and 10 characters",
#     "consist": "Password must consist only of letters and digits",
#     "least": "Password must have at least 2 digits"
# }
#
#
# def password_validation(password):
#     if not 6 <= len(password) <= 10:
#         print(errors.pop("leng"))
#     if not password.isalnum():
#         print(errors.pop("consist"))
#     if sum(1 for x in password if x.isdigit()) < 2:
#         print(errors.pop("least"))
#
#
# current_password = input()
# password_validation(current_password)
# if len(errors) == 3:
#     print("Password is valid")




#
#
# errors = {
#     "leng": "Password must be between 6 and 10 characters",
#     "consist": "Password must consist only of letters and digits",
#     "least": "Password must have at least 2 digits"
# }
#
#
# def password_validation(password):
#     result = []
#     if not 6 <= len(password) <= 10:
#         result.append("leng")
#     if not password.isalnum():
#         result.append("consist")
#     if sum(1 for x in password if x.isdigit()) < 2:
#         result.append("least")
#     return result
#
#
# current_password = input()
# result = password_validation(current_password)
# if result:
#     [print(errors[show]) for show in result]
# else:
#     print("Password is valid")
#
#
#
#
#
#
#
# password_to_check = input()
#
# characters_in_range = False
# letters_digits_only = False
# two_digits = False
# numbers_check = 0
#
#
# def pass_check(check):
#     global characters_in_range, letters_digits_only, two_digits, numbers_check
#     if 6 <= len(check) <= 10:
#         characters_in_range = True
#     if check.isalnum():
#         letters_digits_only = True
#     for letter in check:
#         if letter.isdigit():
#             numbers_check += 1
#         if numbers_check == 2:
#             two_digits = True
#             break
#
#
# pass_check(password_to_check)
#
# if all([characters_in_range, letters_digits_only, two_digits]):
#     print("Password is valid")
# if not characters_in_range:
#     print("Password must be between 6 and 10 characters")
# if not letters_digits_only:
#     print("Password must consist only of letters and digits")
# if not two_digits:
#     print("Password must have at least 2 digits")
