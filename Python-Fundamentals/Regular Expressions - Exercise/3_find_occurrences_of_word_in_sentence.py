import re

main_string = input().lower()
word_to_look_for = input().lower()

patterns = re.compile(r"\b" + word_to_look_for + r"\b")
print(len(list(re.finditer(patterns, main_string))))





#
# import re
# main_string = input().lower()
# find_string = input().lower()
# pattern = re.compile(r"\b"+find_string+r"\b")
# matches = pattern.finditer(main_string)
# show_result = 0
# for show in matches:
#     show_result += 1
#
# print(show_result)
