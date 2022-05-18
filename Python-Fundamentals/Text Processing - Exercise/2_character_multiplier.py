from itertools import zip_longest

first_string, second_string = input().split()
result_ = []

for ltr_one, ltr_two in zip_longest(first_string, second_string, fillvalue="Skip"):
    if "Skip" != ltr_one and "Skip" != ltr_two:
        result_.append(ord(ltr_one) * ord(ltr_two))
    elif "Skip" != ltr_one:
        result_.append(ord(ltr_one))
    elif "Skip" != ltr_two:
        result_.append(ord(ltr_two))

print(sum(result_))
