phone_book = {}
phone_number = input()
while not phone_number.isdigit():
    name, number = phone_number.split("-")
    phone_book[name] = phone_book.get(name, number)
    phone_number = input()

for _ in range(int(phone_number)):
    name_check = input()
    if name_check in phone_book:
        print(f"{name_check} -> {phone_book[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
