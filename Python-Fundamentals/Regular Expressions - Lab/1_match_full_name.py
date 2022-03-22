import re

name_string = input()

find_name = re.compile(r"(\b[A-Z][a-z]+ [A-Z][a-z]+\b)")

# for name in name_string:
#     match_find = re.finditer(find_name, name)
#     for show in match_find:
#         if len(show[0]) == len(name):
#             print(show[0], end=" ")


match_find = re.findall(find_name, name_string)
# print(" ".join(match_find))
print(*match_find, sep= " ")