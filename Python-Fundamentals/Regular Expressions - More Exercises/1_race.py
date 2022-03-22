import re

name_of_participants = {name.replace(" ", ""): 0 for name in input().split(",")}

result_show = []
racer_code = input()
letters_d = re.compile(r"([A-Za-z])")
numbers_d = re.compile(r"([0-9])")
score_d = "score"
name_d = "name"
while racer_code != "end of race":
    find_letters_d = re.finditer(letters_d, racer_code)
    find_numbers_d = re.finditer(numbers_d, racer_code)
    find_name = ""
    find_numbers = 0
    for name in find_letters_d:
        find_name += name[0]
    for numbers in find_numbers_d:
        find_numbers += int(numbers[0])
    if find_name in name_of_participants.keys():
        name_of_participants[find_name] += find_numbers
    racer_code = input()

# result_p = sorted(name_of_participants.items(), key=lambda item: item[1])
for name in name_of_participants:
    result_show.append({name_d: name, score_d: name_of_participants[name]})
result_show.sort(key=lambda item: (-item[score_d]))

print(f"1st place: {result_show[0][name_d]}")
print(f"2nd place: {result_show[1][name_d]}")
print(f"3rd place: {result_show[2][name_d]}")
