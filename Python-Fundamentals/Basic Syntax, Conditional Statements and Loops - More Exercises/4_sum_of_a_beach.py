text = input().lower()
words = ["sand", "water", "fish", "sun"]
print(sum([text.count(word) for word in words]))







#
# text = input()
# counter = 0
# convert_text_to_lower = list(text.lower())
# i = 1
# check_len = len(convert_text_to_lower)
# for word in convert_text_to_lower:
#     if check_len - 2 == i:
#         break
#     check_word = word + convert_text_to_lower[i] + convert_text_to_lower[i + 1] + convert_text_to_lower[i + 2]
#     i += 1
#     if "sand" in check_word:
#         counter += 1
#
#     if "fish" in check_word:
#         counter += 1
#
# check_word = ""
# i = 1
# for word in convert_text_to_lower:
#     if check_len - 1 == i:
#         break
#     check_word = word + convert_text_to_lower[i] + convert_text_to_lower[i + 1]
#     i += 1
#     if "sun" in check_word:
#         counter += 1
#
# check_word = ""
# i = 1
# for word in convert_text_to_lower:
#     if check_len - 3 == i:
#         break
#
#     check_word = word + convert_text_to_lower[i] + convert_text_to_lower[i + 1] + convert_text_to_lower[i + 2] + \
#                  convert_text_to_lower[i + 3]
#     i += 1
#     if "water" in check_word:
#         counter += 1
#
# print(counter)
