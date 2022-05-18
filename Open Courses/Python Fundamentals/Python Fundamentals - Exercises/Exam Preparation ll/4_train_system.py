existing_cards = int(input())

cards_info = {}
result_list = []


def create_user(name, card_number):
    if name not in cards_info:
        cards_info[name] = {"card number": []}
    cards_info[f"{first_name} {last_name}"]["card number"].append(card_number)


def check_card(name, card_number):
    if name in cards_info:
        if card_number in cards_info[name]["card number"]:
            return True
    else:
        return False


def check_card_exist_on_another_user(user_name, card_number):
    for name in cards_info:
        if user_name != name and card_number in cards_info[name]["card number"]:
            return True
    return False


def ticket_price(name, town, discount, card=None, off=1):
    if discount: off = 0.50
    total = sum([ord(x) for x in town]) / 100 * off
    cards_info[name][total] = [{"destination": town, "card id": card}]


def check_valid_card(name, card_number, town):
    total = [int(x) for x in card_number]
    create_user(name, 0)
    if sum(total) % 7 != 0:
        print(f"card {card_number} is not valid!")
        ticket_price(name, town, False)
    else:
        if check_card_exist_on_another_user(name, card_number):
            print(f"card {card_number} already exists for another passenger!")
            ticket_price(name, town, False)
        else:
            if card_number not in cards_info[name]["card number"]:
                create_user(name, card_number)
                print(f"issuing card {card_number}")
            ticket_price(name, town, True, card_number)


for _ in range(existing_cards):
    first_name, last_name, ticket_number = input().split()
    create_user(f"{first_name} {last_name}", ticket_number)
command_ = input()
while command_ != "time to leave!":
    _, first_name, last_name, destination, card_number = command_.split()
    if check_card(f"{first_name} {last_name}", card_number):
        ticket_price(f"{first_name} {last_name}", destination, True, card_number)
    else:
        check_valid_card(f"{first_name} {last_name}", card_number, destination)
    command_ = input()


def show_result():
    for name in cards_info:
        del cards_info[name]["card number"]
        total = [key for key in cards_info[name]]
        result_list.append({'name': name, 'total': sum(total)})
    for show in sorted(result_list, key=lambda x: -x["total"]):
        if show['total'] != 0:
            print(f"{show['name']}:")
            for price, destination in sorted(cards_info[show['name']].items(), key=lambda x: -x[0]):
                card_used = ""
                if None is not destination[0]['card id']:
                    card_used = f" (using card {destination[0]['card id']})"
                print(f"--{destination[0]['destination']}: {price:.2f}lv{card_used}")
            print(f"total: {show['total']:.2f}lv")


show_result()
