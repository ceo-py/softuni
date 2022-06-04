numbers = input().split()
string_text = input()

msg_show = ""
for num in numbers:
    find_index = sum([int(s_num) for s_num in num])
    if find_index > len(string_text):
        find_index = find_index - len(string_text)
    msg_show += string_text[find_index]
    string_text = string_text[:find_index] + string_text[find_index + 1:]

print(msg_show)









#
#
# numbers = [n for n in input().split()]
# string_text = input()
#
# msg_show = ""
#
# for num in numbers:
#     find_index = 0
#     for s_num in num:
#         find_index += int(s_num)
#     if find_index > len(string_text):
#         find_index = find_index - len(string_text)
#     msg_show += string_text[find_index]
#     string_text = string_text[:find_index] + string_text[find_index + 1:]
#
# print(msg_show)
