import re

main_string = input()
all_digits = ''.join(x for x in main_string if x.isdigit())
cool_threshold = 1
for num in all_digits:
    cool_threshold *= int(num)


print(f"Cool threshold: {cool_threshold}")
patterns = re.compile(r"(::)(?P<emoji>[A-Z][a-z]{2,})(::)|(\*\*)(?P<emoji2>[A-Z][a-z]{2,})(\*\*)")
main_string = list(re.finditer(patterns, main_string))
print(f"{len(main_string)} emojis found in the text. The cool ones are:")
for found in main_string:
    if found["emoji"]:
        result = found["emoji"]
    elif found["emoji2"]:
        result = found["emoji2"]

    find_cool = sum([ord(letter) for letter in result])
    if find_cool >= cool_threshold:
        print(found[0])






#
#
#
# import re
#
# main_string = input()
#
# find_numbers = ''.join([num for num in main_string if num.isdigit()])
# total_sum_numbers = 1
# for num in find_numbers:
#     total_sum_numbers *= int(num)
#
# patterns = re.compile(r"\:{2}([A-Z]{1}[a-z]{2,})\:{2}|\*{2}([A-Z]{1}[a-z]{2,})\*{2}")
# find_emoji = re.finditer(patterns, main_string)
# resul_to_print = []
# for find_number, show in enumerate(find_emoji):
#     asci_value = 0
#     group = 1
#     if show[1] is None:
#         group = 2
#     asci_value = sum([ord(letter) for letter in show[group]])
#     if asci_value > total_sum_numbers:
#         resul_to_print.append(show[0])
#
# print(f"Cool threshold: {total_sum_numbers}")
# print(f"{find_number + 1} emojis found in the text. The cool ones are:")
# print(*resul_to_print, sep="\n")
#
#
#
#
#
#
#
#


#
# import re
#
# main_string = input()
#
# find_numbers = ""
#
# for num in main_string:
#     if num.isdigit():
#         find_numbers += num
# total_sum_numbers = 1
# for num in find_numbers:
#     total_sum_numbers *= int(num)
#
# patterns = re.compile(r"\:{2}([A-Z]{1}[a-z]{2,})\:{2}|\*{2}([A-Z]{1}[a-z]{2,})\*{2}")
# find_emoji = re.finditer(patterns, main_string)
# resul_to_print = []
# for find_number, show in enumerate(find_emoji):
#     asci_value = 0
#     if show[1] is None:
#         for letter in show[2]:
#             asci_value += ord(letter)
#     else:
#         for letter in show[1]:
#             asci_value += ord(letter)
#     if asci_value > total_sum_numbers:
#         resul_to_print.append(show[0])
#
# print(f"Cool threshold: {total_sum_numbers}")
# print(f"{find_number + 1} emojis found in the text. The cool ones are:")
# print(*resul_to_print, sep="\n")
