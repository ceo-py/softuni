import re

main_string = input()
patterns = re.compile(
    r"([=/])(?P<location>[A-Z][a-zA-Z]{2,})\1")
list_result = list()
result = re.finditer(patterns, main_string)
total_points = 0
for show in result:
    list_result.append(show["location"])
    total_points += len(show["location"])

print(f"Destinations: {', '.join(list_result)}")
print(f"Travel Points: {total_points}")




#
# import re
#
# main_string = input()
# patterns = re.compile(r"[=|/]([A-Z][a-zA-Z]+)[=|/]")
# list_result = list()
# main_string = re.finditer(patterns, main_string)
# total_points = 0
# for show in main_string:
#     count_items = show[0].count("=")
#     count_items_two = show[0].count("/")
#     letters_count = len(show[1])
#     if (count_items == 2 or count_items_two == 2) and letters_count >= 3:
#         list_result.append(show[1])
#         total_points += len(show[1])
#
# print("Destinations: ", end="")
# print(*list_result, sep=", ")
# print(f"Travel Points: {total_points}")
