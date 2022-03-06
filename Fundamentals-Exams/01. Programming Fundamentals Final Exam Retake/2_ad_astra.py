import re

main_string = input()

name_r = "name"
date_r = "date"
nutrition_r = "nutrition"
patterns = re.compile(r"[#|\|]([a-zA-Z ]+)[#|\|](\d\d/\d\d/\d\d)[#|\|](\d+)[#|\|]")
list_result = list()
main_string = re.finditer(patterns, main_string)
total = 0
for show in main_string:
    dash = show[0].count("#")
    special_s = show[0].count("|")
    if dash == 4 or special_s == 4:
        name_d = show[1]
        date_d = show[2]
        nutrition_d = show[3]
        total += int(nutrition_d)
        list_result.append({"name": name_d, "date": date_d, "nutrition": nutrition_d})

total = int(total / 2000)

print(f"You have food to last you for: {total} days!")
for show in list_result:
    print(f"Item: {show[name_r]}, Best before: {show[date_r]}, Nutrition: {show[nutrition_r]}")
