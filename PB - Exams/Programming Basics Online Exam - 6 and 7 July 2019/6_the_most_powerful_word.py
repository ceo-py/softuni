import math

word = input()

most_powerful_word = ''
most_powerful_points = 0

letters_to_double =  'aeiouy'


while word != 'End of words':

    current_word_points = 0

    for letter in word:

        current_word_points += int(ord(letter))

    if word[0] in f'{letters_to_double}{letters_to_double.upper()}':
        current_word_points *= len(word)
    else:
        current_word_points =  math.floor(current_word_points / len(word))

    if current_word_points > most_powerful_points:
        most_powerful_word = word
        most_powerful_points = current_word_points

    word = input()

print(f'The most powerful word is {most_powerful_word} - {most_powerful_points}')







# import math
#
# word_enter = input()
# most_powerful_word, points, how_long_is_the_word, letters_ = "", 0, 0, "aeiouy"
#
# while word_enter != "End of words":
#     total_word_points, first_letter = 0, word_enter[0]
#     how_long_is_the_word = len(word_enter)
#     for letter in word_enter:
#         total_word_points += int(ord(letter))
#
#     if first_letter in letters_ or first_letter in letters_.upper():
#         total_word_points *= how_long_is_the_word
#     else:
#         total_word_points = math.floor(total_word_points / how_long_is_the_word)
#
#     if total_word_points > points:
#         points = total_word_points
#         most_powerful_word = word_enter
#
#     word_enter = input()
#
# print(f"The most powerful word is {most_powerful_word} - {points}")




#
#
# import math
#
# word_enter = input()
# most_powerful_word = ""
# points = 0
# how_long_is_the_word = 0
#
# while word_enter != "End of words":
#     counter = 0
#     total_word_points = 0
#     bonus_points = False
#
#     how_long_is_the_word = len(word_enter)
#     for letter in word_enter:
#         counter += 1
#         letters_ = "aeiouy"
#         if (letter in letters_ or letter in letters_.upper()) and counter == 1:
#             bonus_points = True
#
#         total_word_points += int(ord(letter))
#
#     if bonus_points:
#         total_word_points *= how_long_is_the_word
#
#     else:
#         total_word_points = math.floor(total_word_points / how_long_is_the_word)
#
#     if total_word_points > points:
#         points = total_word_points
#         most_powerful_word = word_enter
#
#     word_enter = input()
#
# print(f"The most powerful word is {most_powerful_word} - {points}")
#


#
#
# import math
#
# end_of_last_world = True
# most_powerfull_word = ""
# points = 0
# how_long_is_the_word = 0
#
#
# while end_of_last_world:
#     word_enter = input()
#     counter = 0
#     total_word_points = 0
#     bonus_points = False
#
#     if word_enter == "End of words":
#         print(f"The most powerful word is {most_powerfull_word} - {points}")
#         end_of_last_world = False
#
#     else:
#         how_long_is_the_word = len(word_enter)
#         for letter in word_enter:
#             counter += 1
#             if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y" or \
#                     letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "Y") and counter == 1:
#                 bonus_points = True
#
#             total_word_points += int(ord(letter))
#
#         if bonus_points:
#             total_word_points *= how_long_is_the_word
#
#         else:
#             total_word_points = math.floor(total_word_points / how_long_is_the_word)
#
#         if total_word_points > points:
#             points = total_word_points
#             most_powerfull_word = word_enter
#
