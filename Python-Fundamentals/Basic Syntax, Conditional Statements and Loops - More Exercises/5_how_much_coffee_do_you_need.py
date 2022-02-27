import string

cofee_count = 0

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
events_to_check = ["d", "c", "C", "m", "D", "M"]

while True:
    event = input()
    if event == "END":
        break

    if event[0] in upper_letters and event[0] in events_to_check:
        cofee_count += 2

    elif event[0] in lower_letters and event[0] in events_to_check:
        cofee_count += 1

    if cofee_count > 5:
        text_to_print = "You need extra sleep"

if cofee_count > 5:
    print(text_to_print)

else:
    print(cofee_count)
