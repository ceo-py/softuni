import re

main_string = input()

patterns = re.compile(r"\b_(?P<word>[A-Za-z0-9]+\b)")
result = re.finditer(patterns, main_string)
result_show = []
for show in result:
    result_show.append(show["word"])

print(','.join(result_show))




#
#
#
# import re
#
# main_string = input()
# pattern = re.compile(r"\b_([a-zA-Z0-9]+)\b")
# matches = pattern.finditer(main_string)
# show_result = []
# for show in matches:
#     show_result.append(show[1])
#
# print(",".join(show_result))