string_expression = input()

per_stack = []

for index, char in enumerate(string_expression):
    if char == "(":
        per_stack.append(index)
    elif char == ")":
        start_index = per_stack.pop()
        print(string_expression[start_index:1+index])


# for index in range(len(string_expression)):
#     if string_expression[index] == "(":
#         per_stack.append(index)
#     elif string_expression[index] == ")":
#         start_index = per_stack.pop()
#         print(string_expression[start_index:1 + index])