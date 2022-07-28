import re

pattern = re.compile(
    r"www.([A-Za-z0-9\-]+)(\.[a-z]+)+")

while True:
    main_string = input()
    if main_string:
        result = re.finditer(pattern, main_string)
        for show in result:
            print(show[0])
    else:
        break






#
#
#
# import re
# pattern = re.compile(r"\bwww\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*\b")
# while True:
#     main_string = input()
#     if main_string:
#         matches = pattern.finditer(main_string)
#         for show in matches:
#             print(show[0])
#     else:
#         break
