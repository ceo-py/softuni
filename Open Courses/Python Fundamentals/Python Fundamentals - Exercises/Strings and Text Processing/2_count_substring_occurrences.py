import re
text = input().lower()
print(len(re.findall(rf'(?=({input().lower()}))', text)))



#
#
# def frequency_count(string, substr):
#     count, pos = 0, 0
#     while True:
#         pos = string.find(substr, pos)
#         if pos > -1:
#             count += 1
#             pos += 1
#         else:
#             break
#     return count
#
#
# print(frequency_count(input().lower(), input().lower()))



# print(input().lower().count(input().lower()))




