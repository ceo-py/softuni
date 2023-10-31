n = int(input())
symbols = ".,_"

for words in range(n):
    string_to_input = input()
    if any(x in string_to_input for x in symbols):
        print(f"{string_to_input} is not pure!")
    else:
        print(f"{string_to_input} is pure.")



#
# n = int(input())
# symbols = ".,_"
#
# for words in range(n):
#     string_to_input = input()
#     print(f"{string_to_input} is not pure!" if any(x in string_to_input for x in symbols) else f"{string_to_input} is pure.")
#



# how_many_strings = int(input())
#
# skip_parameters = [",", ".", "_"]
#
# for _ in range(how_many_strings):
#     string_ = input()
#     for element in skip_parameters:
#         if element in string_:
#             print(f"{string_} is not pure!")
#             break
#     else:
#         print(f"{string_} is pure.")
