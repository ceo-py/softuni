import re

number_of_msg = int(input())

pattern = re.compile(r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1: \[(?P<num1>[\d]+)\]\|\[(?P<num2>[\d]+)\]\|\[(?P<num3>[\d]+)\]\|$")

for _ in range(number_of_msg):
    msg_to_decrypt = input()
    successful_decrypt = ""
    result = list(pattern.finditer(msg_to_decrypt))
    for show in result:
        first, second, third = show["num1"], show["num2"], show["num3"]
        successful_decrypt = f"{chr(int(first))}{chr(int(second))}{chr(int(third))}"
        print(f"{show['tag']}: {successful_decrypt}")
    if not result:
        print("Valid message not found!")