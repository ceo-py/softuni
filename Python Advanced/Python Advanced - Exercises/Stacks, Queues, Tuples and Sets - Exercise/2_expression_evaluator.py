from collections import deque

string_expression = deque(input().split())

result = 0
numbers_so_far = ""
el = 0
while len(string_expression) != 1:
    check_element = string_expression[el]
    if check_element == "-":
        result = int(string_expression.popleft())
        while True:
            check_element = string_expression[0]
            if check_element != "-":
                take_element = string_expression.popleft()
                result -= int(take_element)
            else:
                string_expression[0] = result
                el = 0
                break
    elif check_element == "*":
        result = int(string_expression.popleft())
        while True:
            check_element = string_expression[0]
            if check_element != "*":
                take_element = string_expression.popleft()
                result *= int(take_element)
            else:
                string_expression[0] = result
                el = 0
                break
    elif check_element == "/":
        result = int(string_expression.popleft())
        while True:
            check_element = string_expression[0]
            if check_element != "/":
                take_element = string_expression.popleft()
                result = int(result / int(take_element))
            else:
                string_expression[0] = result
                el = 0
                break
    if check_element == "+":
        result = int(string_expression.popleft())
        while True:
            check_element = string_expression[0]
            if check_element != "+":
                take_element = string_expression.popleft()
                result += int(take_element)
            else:
                string_expression[0] = result
                el = 0
                break
    else:
        el += 1


print(*string_expression)

