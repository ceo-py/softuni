import re

main_string = input()

patterns = re.compile(r"([@#])(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1")
list_result = list()
result = list(re.finditer(patterns, main_string))

for show in result:
    if show["word"] == show["word2"][::-1]:
        list_result.append(f"{show['word']} <=> {show['word2']}")

if result:
    print(f"{len(result)} word pairs found!")
    if list_result:
        print("The mirror words are:")
        print(*list_result, sep=", ")
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")

#
#
#
# import re
#
# main_string = input()
#
# first_word = "first"
# second_word = "second"
# patterns = re.compile(r"\#{1}([A-z]{3,})\#{2}([A-z]{3,})\#{1}|\@{1}([A-z]{3,})\@{2}([A-z]{3,})\@{1}")
# list_result = list()
# main_string = re.finditer(patterns, main_string)
# total_words_found = 0
# find_match = False
# for show in main_string:
#     total_words_found += 1
#     if show[4] is None and show[1] == show[2][::-1]:
#         list_result.append({first_word: show[1], second_word: show[2]})
#         if not find_match:
#             find_match = True
#     elif show[1] is None and show[3] == show[4][::-1]:
#         list_result.append({first_word: show[3], second_word: show[4]})
#         if not find_match:
#             find_match = True
#
# if total_words_found != 0 and not find_match:
#     print(f"{total_words_found} word pairs found!")
#     print("No mirror words!")
# elif find_match:
#     print(f"{total_words_found} word pairs found!")
#     print("The mirror words are:")
#     for index, show in enumerate(list_result):
#         if index != len(list_result) - 1:
#             print(f"{show[first_word]} <=> {show[second_word]}", end=", ")
#         else:
#             print(f"{show[first_word]} <=> {show[second_word]}", end="")
# else:
#     print("No word pairs found!")
#     print("No mirror words!")
