import re

letter_to_find = input()

pattern = re.compile(f"[A-Za-z]+")
allow_end_char = ["?", "!", "."]
data_input = input()
result_list = []
while data_input != "end":
    matches = pattern.finditer(data_input)
    if data_input[0].isupper() and data_input[-1] in allow_end_char:
        for show in matches:
            if int(letter_to_find[1]) <= show[0].count(letter_to_find[0]):
                result_list.append(show[0])
    data_input = input()

print(", ".join(result_list))