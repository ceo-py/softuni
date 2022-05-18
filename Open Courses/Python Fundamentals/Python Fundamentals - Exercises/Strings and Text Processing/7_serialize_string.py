main_string = input()

dic_ = {}
for pos, ltr in enumerate(main_string):
    if ltr not in dic_:
        dic_[ltr] = []
    dic_[ltr].append(str(pos))

[print(f"{ltr}:{'/'.join(pos)}") for ltr, pos in dic_.items()]






# main_string = input()
# banned_letters = []
# for ltr in main_string:
#     show_result = []
#     if ltr not in banned_letters:
#         banned_letters.append(ltr)
#         for pos in range(len(main_string)):
#             if ltr == main_string[pos]:
#                 show_result.append(str(pos))
#         print(f"{ltr}:{'/'.join(show_result)}")
