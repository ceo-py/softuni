import string

usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char not in "-_" + string.ascii_letters + string.digits:
                break

        else:
            print(username)






#
#
# test_string = input().split(", ")
#
# for test in test_string:
#     if 3 <= len(test) <= 16:
#         for check in test:
#             if not any([check.isdigit(), check.isalpha(), check == "-", check == "_"]):
#                 break
#         else:
#             print(test)
