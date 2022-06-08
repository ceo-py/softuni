start_char, end_char, random_string = input(), input(), input()

print(sum([ord(char) for char in random_string if ord(start_char) < ord(char) < ord(end_char)]))





# start_char, end_char, random_string = input(), input(), input()
#
# show_result = 0
# for character in random_string:
#     if ord(start_char) < ord(character) < ord(end_char):
#         show_result += ord(character)
#
# print(show_result)
