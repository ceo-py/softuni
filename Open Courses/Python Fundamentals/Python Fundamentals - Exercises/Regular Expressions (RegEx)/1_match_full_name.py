import re

name_string = input()

find_name = re.compile(r"(\b[A-Z][a-z]+ [A-Z][a-z]+\b)")
match_find = re.findall(find_name, name_string)
print(*match_find, sep= " ")