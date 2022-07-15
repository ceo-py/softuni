first_text = input()
second_text = input()

for index in range(len(first_text)):
    if first_text[index] != second_text[index]:
        first_text = second_text[:index + 1] + first_text[index + 1:]
        print(first_text)







#
#
# first_text = [n for n in input()]
# second_text = [n for n in input()]
#
# target_list = list(first_text)
#
# for index, (letter_a, letter_b) in enumerate(zip(first_text, second_text)):
#     if letter_a != letter_b:
#         target_list[index] = letter_b
#         for letter in target_list:
#             print(f"{letter}", end="")
#         print()
#
#


# first_text = input()
# second_text = input()
#
# list_one = list(first_text)
# list_two = list(second_text)
# i = 0
# target_list = list(first_text)
#
# for letter_a, letter_b in zip(list_one, list_two):
#     if letter_a != letter_b:
#         target_list[i] = letter_b
#         for _ in target_list:
#             print(f"{_}", end="")
#         print()
#     i += 1
