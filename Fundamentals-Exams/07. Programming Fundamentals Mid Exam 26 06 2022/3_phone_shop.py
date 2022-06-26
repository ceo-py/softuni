phone_models = input().split(", ")
command = input()


def add_phone(phone):
    if phone not in phone_models:
        phone_models.append(phone)


def remove_phone(phone):
    if phone in phone_models:
        phone_models.remove(phone)


def bonus_phone(old_phone, new_phone):
    if old_phone in phone_models:
        phone_models.insert(phone_models.index(old_phone) + 1, new_phone)


def last_phone(phone):
    if phone in phone_models:
        phone_models.append(phone_models.pop(phone_models.index(phone)))


while command != "End":
    if "Bonus phone" not in command:
        command_type, phone = command.split(" - ")
    else:
        command_type, phones = command.split(" - ")
        old_phone, new_phone = phones.split(":")
        bonus_phone(old_phone, new_phone)
    if "Add" in command_type:
        add_phone(phone)
    elif "Remove" in command_type:
        remove_phone(phone)
    elif "Last" in command_type:
        last_phone(phone)

    command = input()

print(", ".join(phone_models))
