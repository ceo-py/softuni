import re

number_of_msg = int(input())

pattern = re.compile(r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1: "
                     r"\[(?P<num1>[\d]+)"
                     r"\]\|\[(?P<num2>[\d]+)"
                     r"\]\|\[(?P<num3>[\d]+)\]\|$")

for _ in range(number_of_msg):
    msg_to_decrypt = input()
    result = list(pattern.finditer(msg_to_decrypt))
    for show in result:
        successful_decrypt = f'{chr(int(show["num1"]))}{chr(int(show["num2"]))}{chr(int(show["num3"]))}'
        print(f"{show['tag']}: {successful_decrypt}")
    if not result:
        print("Valid message not found!")