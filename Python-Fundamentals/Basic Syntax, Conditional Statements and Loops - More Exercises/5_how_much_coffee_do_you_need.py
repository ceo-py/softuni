cafe_count = 0
events_to_check = ["d", "c", "C", "m", "D", "M"]
event = input()
while event != "END":
    if event[0].isupper() and event[0] in events_to_check:
        cafe_count += 2
    elif event[0].islower() and event[0] in events_to_check:
        cafe_count += 1
    if cafe_count > 5:
        text_to_print = "You need extra sleep"
    event = input()

if cafe_count > 5:
    print(text_to_print)

else:
    print(cafe_count)


# import string
#
# cofee_count = 0
#
# upper_letters = string.ascii_uppercase
# lower_letters = string.ascii_lowercase
# events_to_check = ["d", "c", "C", "m", "D", "M"]
#
# while True:
#     event = input()
#     if event == "END":
#         break
#
#     if event[0] in upper_letters and event[0] in events_to_check:
#         cofee_count += 2
#
#     elif event[0] in lower_letters and event[0] in events_to_check:
#         cofee_count += 1
#
#     if cofee_count > 5:
#         text_to_print = "You need extra sleep"
#
# if cofee_count > 5:
#     print(text_to_print)
#
# else:
#     print(cofee_count)
