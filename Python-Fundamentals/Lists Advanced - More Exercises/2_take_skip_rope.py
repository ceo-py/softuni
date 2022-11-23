main_string = input()

numbers, letters, output = [], [], []
[numbers.append(int(x)) if x.isdigit() else letters.append(x) for x in main_string]
while numbers:
    take, skip = numbers.pop(0), numbers.pop(0)

    # for x in range(0, len(numbers), 2): - no while loop / this is faster method
    #     take, skip = numbers[x], numbers[x + 1]

    output += letters[:take]
    letters = letters[take + skip:]

print(*output, sep="")







#
# main_string = input()
#
# numbers = list()
# letter = ""
# take_list = list()
# skip_list = list()
#
# result = ""
#
# for character in main_string:
#     if character.isdigit():
#         numbers.append(int(character))
#     else:
#         letter += character
#
# for ind, num in enumerate(numbers):
#     if ind % 2 == 0:
#         take_list.append(num)
#     else:
#         skip_list.append(num)
#
# for i, n in zip(take_list, skip_list):
#     if i == 0:
#         letter = letter[n:]
#     elif i != 0:
#         result = result + letter[:i]
#         letter = letter[n + i:]
#
# print(result)
