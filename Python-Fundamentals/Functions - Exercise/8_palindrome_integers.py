def check_palindrome(numbers):
    [print(n == n[::-1]) for n in numbers]

check_palindrome(input().split(", "))




# [print(n == n[::-1]) for n in input().split(", ")]




# main_list = input().split(", ")
#
#
# def check_palindrome(numbers):
#     for n in numbers:
#         if n == n[::-1]:
#             print("True")
#         else:
#             print("False")
#
#
# check_palindrome(main_list)
