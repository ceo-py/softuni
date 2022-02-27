phone_book = {}
phone_number = input()
while not phone_number.isdigit():
    phone_number = phone_number.split("-")
    name = phone_number[0]
    number = phone_number[-1]
    if name not in phone_book:
        phone_book[name] = 0
    phone_book[name] = number
    phone_number = input()

for _ in range(int(phone_number)):
    name_check = input()
    if name_check in phone_book:
        print(f"{name_check} -> {phone_book[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
