import re

main_string = input()

patterns = re.compile(r"\+359([ -])2\1([0-9]{3})\1([0-9]{4})\b")
list_result = list()
result = re.finditer(patterns, main_string)

for show in result:
    list_result.append(show[0])

print(*list_result, sep=", ")





# import re
#
# phone_number = input()
# pattern = re.compile(r"((^\+|\s\+)359-2-\d{3}-\b\d{4}\b|(^\+|\s\+)359\s2\s\d{3}\s\b\d{4}\b)")
# matches = pattern.finditer(phone_number)
# show_result = []
# for show in matches:
#     show_result.append(show[0])
#
# print(",".join(show_result))
