main_string = input()
check_string = input()
result_sum = 0
for ltr in main_string:
    if check_string == "UPPERCASE" and ltr.isupper() or check_string == "LOWERCASE" and ltr.islower():
        result_sum += ord(ltr)

print(f"The total sum is: {result_sum}")
