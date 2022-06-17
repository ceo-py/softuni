command = input()

result = []

while command != "End":
    pos, task = command.split("-")
    result.append([int(pos), task])
    command = input()

print([to_do[1] for to_do in sorted(result, key=lambda x: x[0])])











#
#
# main_list = [0] * 10
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     tokents = command.split("-")
#     priority = int(tokents[0]) - 1
#     note = tokents[1]
#     main_list.pop(priority)
#     main_list.insert(priority, note)
#
# result = [n for n in main_list if n != 0]
# print(result)
