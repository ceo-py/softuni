first_string, second_string = input().split()

first_string = [ord(num) for num in first_string]
second_string = [ord(num) for num in second_string]
first_string_len = len(first_string)
second_string_len = len(second_string)
if first_string_len > second_string_len:
    for _ in range(first_string_len - second_string_len):
        second_string.append(1)
elif first_string_len < second_string_len:
    for _ in range(second_string_len - first_string_len):
        first_string.append(1)
print(sum([first_string[i] * second_string[i] for i in range(len(first_string))]))


# from itertools import zip_longest

# first_string, second_string = input().split()
# result_ = []
#
# for ltr_one, ltr_two in zip_longest(first_string, second_string, fillvalue="Skip"):
#     if ltr_one != "Skip" != ltr_two:
#         result_.append(ord(ltr_one) * ord(ltr_two))
#     elif "Skip" != ltr_one:
#         result_.append(ord(ltr_one))
#     elif "Skip" != ltr_two:
#         result_.append(ord(ltr_two))
#
# print(sum(result_))
