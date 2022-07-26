import re

main_string = input()

patterns = re.compile(r"(?P<Day>[0-9]{2})([\.\-/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>[0-9]{4})\b")
result = re.finditer(patterns, main_string)

for show in result:
    print(f"Day: {show['Day']}, Month: {show['Month']}, Year: {show['Year']}")








#
# import re
#
# dates_match = input()
# pattern = re.compile(
#     r"(\d{2}-[A-Z]{1}[a-z]{2}-\b\d{4}\b|\d{2}\.[A-Z]{1}[a-z]{2}\.\b\d{4}\b|\d{2}/[A-Z]{1}[a-z]{2}/\b\d{4}\b)")
# matches = pattern.finditer(dates_match)
# for show in matches:
#     if "/" in show[0]:
#         show = show[0].split("/")
#     elif "-" in show[0]:
#         show = show[0].split("-")
#     elif "." in show[0]:
#         show = show[0].split(".")
#     print(f"Day: {show[0]}, Month: {show[1]}, Year: {show[2]}")
