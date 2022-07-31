letter = input()

complete_word, skip_letters_count, guess_word = "",  "",  ""
while letter != "End":
    if letter in "con":
        skip_letters_count += letter
    elif letter.islower() or letter.isupper():
        guess_word += letter
    if "c" in skip_letters_count and "o" in skip_letters_count and "n" in skip_letters_count:
        complete_word += f"{guess_word} "
        guess_word, skip_letters_count = "", ""
    if skip_letters_count.count(letter) > 1:
        guess_word += letter
    letter = input()

print(complete_word)




#
# skip_letters = "con"
#
# letter = input()
# complete_word = ""
# skip_letters_count = ""
# guess_word = ""
# while letter != "End":
#     if letter in skip_letters:
#         skip_letters_count += letter
#     else:
#         if letter.islower() or letter.isupper():
#             guess_word += letter
#     if "c" in skip_letters_count and "o" in skip_letters_count and "n" in skip_letters_count:
#         skip_letters_count = ""
#         complete_word += f"{guess_word} "
#         guess_word = ""
#     if skip_letters_count.count(letter) > 1:
#         guess_word += letter
#
#     letter = input()
#
# print(complete_word)
#
#




# is_loop_exit = False
# is_c = False
# is_o = False
# is_n = False
#
# cuttent_string = ""
# result_string = ""
#
# while (not is_loop_exit):
#     input_string = input()
#
#     if input_string.lower() == "end":
#         is_loop_exit = True
#     else:
#         if input_string == "c" and not is_c:
#             is_c = True
#         elif input_string == "o" and not is_o:
#             is_o = True
#         elif input_string == "n" and not is_n:
#             is_n = True
#         else:
#             if input_string.isalpha():
#                 cuttent_string = f"{cuttent_string}{input_string}"
#
#         is_code_complete = (is_n and is_o and is_c)
#         if (is_code_complete):
#             result_string = f"{result_string}{cuttent_string} "
#             cuttent_string = ""
#             is_c = False
#             is_o = False
#             is_n = False
#
# print(result_string)


# import string
#
# saved_letter = list()
# guess_word = ""
# skip_letters = ["c", "o", "n"]
# skip_letters_one_time = list()
# complete_word = list()
# lower_letters = string.ascii_lowercase
# upper_letters = string.ascii_uppercase
#
# while True:
#     letter = input()
#     saved_letter.append(letter)
#     if letter == "End":
#         break
#     if letter in skip_letters:
#         skip_letters_one_time.append(letter)
#     else:
#         if letter in lower_letters or letter in upper_letters:
#             guess_word += letter
#     if "c" in skip_letters_one_time and "o" in skip_letters_one_time and "n" in skip_letters_one_time:
#         skip_letters_one_time.clear()
#         complete_word.append(guess_word)
#         guess_word = " "
#     for char in skip_letters_one_time:
#         count = skip_letters_one_time.count(letter)
#         if count > 1:
#             guess_word += letter
#             break
# for word in complete_word:
#     print(word, end="")
