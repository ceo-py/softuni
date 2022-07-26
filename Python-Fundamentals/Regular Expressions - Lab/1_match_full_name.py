import re

name_string = input()

find_name = re.compile(r"(\b[A-Z][a-z]+ [A-Z][a-z]+\b)")
match_find = re.findall(find_name, name_string)
print(*match_find, sep= " ")


# import re
#
# main_string = input()
#
# patterns = re.compile(r"\b(?P<word>[A-Z][a-z]{1,}) (?P<word2>[A-Z][a-z]{1,})\b")
# list_result = list()
# result = re.finditer(patterns, main_string)
#
# for show in result:
#     list_result.append(f"{show['word']} {show['word2']}")
#
# print(*list_result)
#
#
#











