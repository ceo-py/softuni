main_list = input().split(", ")


def check_palindrome(numbers):
    for n in numbers:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


check_palindrome(main_list)
