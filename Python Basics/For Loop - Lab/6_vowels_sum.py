text_input = input()

summary = 0

for letter in text_input:

    if letter == 'a':
        summary += 1

    elif letter == 'e':
        summary += 2

    elif letter == 'i':
        summary += 3

    elif letter == 'o':
        summary += 4

    elif letter == 'u':
        summary += 5

print(summary)





# text_input = input()
#
# letters = {
#     "a": 1,
#     "e": 2,
#     "i": 3,
#     "o": 4,
#     "u": 5
# }
# summary = 0
# for letter in text_input:
#     summary += letters.get(letter, 0)
# print(summary)