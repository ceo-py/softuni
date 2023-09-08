words = input().lower().split()

output = {}
for word in words:
    output[word] = output.get(word, 0) + 1

for word, quantity in output.items():
    if quantity % 2 != 0:
        print(word, end=' ')







# elements = input().lower().split()
#
# # split_elements = elements.split()
# # check_element = list()
# # for element in split_elements:
# #     count = split_elements.count(element)
# #     if count % 2 != 0 and element not in check_element:
# #         print(element, end= " ")
# #         check_element.append(element)
#
# elements_dic = dict()
#
# for character in elements:
#     if character not in elements_dic:
#         elements_dic[character] = 0
#     elements_dic[character] += 1
#
# for key, value in elements_dic.items():
#     if value % 2 != 0:
#         print(key, end= " ")






