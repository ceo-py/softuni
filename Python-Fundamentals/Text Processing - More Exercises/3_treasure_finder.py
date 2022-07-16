secret_key = [int(x) for x in input().split()]
secret_msg = input()

how_long = len(secret_key)
while secret_msg != "find":
    secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
    item = secret_text.split("&")[-2]
    location = secret_text.split("<")[-1][:-1]
    print(f"Found {item} at {location}")
    secret_msg = input()







#
#
#
#
# import re
# secret_key = [int(x) for x in input().split()]
# secret_msg = input()
#
# how_long = len(secret_key)
# pattern = re.compile(r"&(.+)&.+<(.+)>")
# while secret_msg != "find":
#     decode_msg = ""
#     index_key = 0
#     for x in secret_msg:
#         decode_msg += chr(ord(x) - secret_key[index_key])
#         index_key += 1
#         if index_key >= how_long:
#             index_key = 0
#     matches = pattern.finditer(decode_msg)
#     for show in matches:
#         print(f"Found {show[1]} at {show[2]}")
#     secret_msg = input()
