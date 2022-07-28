import re

name_of_participants = {name.replace(" ", ""): 0 for name in input().split(",")}
racer_code = input()
letters_d = re.compile(r"([A-Za-z])")
numbers_d = re.compile(r"([0-9])")
while racer_code != "end of race":
    find_name = "".join(re.findall(letters_d, racer_code))
    find_numbers = sum(int(num) for num in re.findall(numbers_d, racer_code))
    if find_name in name_of_participants.keys():
        name_of_participants[find_name] += find_numbers
    racer_code = input()

name_of_participants = sorted(name_of_participants.items(), key=lambda x: -x[1])

print(f"1st place: {name_of_participants[0][0]}")
print(f"2nd place: {name_of_participants[1][0]}")
print(f"3rd place: {name_of_participants[2][0]}")



# names_info = {x: 0 for x in input().split(", ")}
#
# info = input()
# while info != "end of race":
#     name, distance = "", []
#
#     for char in info:
#         if char.isdigit():
#             distance.append(int(char))
#         elif char.isalpha():
#             name += char
#
#     if name in names_info:
#         names_info[name] += sum(distance)
#     info = input()
#
#
# names_info = sorted(names_info.items(), key=lambda x: -x[1])
#
# print(f"1st place: {names_info[0][0]}")
# print(f"2nd place: {names_info[1][0]}")
# print(f"3rd place: {names_info[2][0]}")
#
#
#
#
#







#
#
# import re
#
# name_of_participants = {name.replace(" ", ""): 0 for name in input().split(",")}
#
# result_show = []
# racer_code = input()
# letters_d = re.compile(r"([A-Za-z])")
# numbers_d = re.compile(r"([0-9])")
# score_d = "score"
# name_d = "name"
# while racer_code != "end of race":
#     find_letters_d = re.finditer(letters_d, racer_code)
#     find_numbers_d = re.finditer(numbers_d, racer_code)
#     find_name = ""
#     find_numbers = 0
#     for name in find_letters_d:
#         find_name += name[0]
#     for numbers in find_numbers_d:
#         find_numbers += int(numbers[0])
#     if find_name in name_of_participants.keys():
#         name_of_participants[find_name] += find_numbers
#     racer_code = input()
#
# for name in name_of_participants:
#     result_show.append({name_d: name, score_d: name_of_participants[name]})
# result_show.sort(key=lambda item: (-item[score_d]))
#
# print(f"1st place: {result_show[0][name_d]}")
# print(f"2nd place: {result_show[1][name_d]}")
# print(f"3rd place: {result_show[2][name_d]}")
