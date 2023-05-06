main_events = input().split("|")

energy = 100
coins = 100


def rest_event(energy_number, energy):
    if energy + energy_number > 100:
        energy_number = abs(100 - energy)

    energy += energy_number
    print(f"You gained {energy_number} energy.")
    print(f"Current energy: {energy}.")
    return energy


def order_event(coins_number, coins, energy):
    if energy - 30 >= 0:
        coins += coins_number
        energy -= 30
        print(f"You earned {coins_number} coins.")
    else:
        print("You had to rest!")
        energy += 50
    return energy, coins


def ingredient_event(name, price_item, coins):
    if price_item <= coins:
        print(f"You bought {name}.")
        coins -= price_item
        return coins

    print(f"Closed! Cannot afford {name}.")
    exit()


for event_type in main_events:
    event_type = event_type.split("-")
    event_command = event_type[0]
    event_energy_coins = int(event_type[-1])

    if event_command == "rest":
        energy = rest_event(event_energy_coins, energy)
    elif event_command == "order":
        energy, coins = order_event(event_energy_coins, coins, energy)
    else:
        coins = ingredient_event(event_command, event_energy_coins, coins)

print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")




# commands_list = input().split("|")
# gained_energy, current_energy, coins = 0, 100, 100
#
# for command in commands_list:
#     current_event = []
#     event_value = 0
#     for element in command.split("-"):
#         current_event.append(element)
#     event_value = int(current_event[-1])
#     if "rest" in current_event:
#         if current_energy + event_value > 100:
#             print(f"You gained {abs(100 - current_energy)} energy.")
#             current_energy = 100
#         else:
#             current_energy += event_value
#             print(f"You gained {event_value} energy.")
#         print(f"Current energy: {current_energy}.")
#
#     elif "order" in current_event:
#         if current_energy >= 30:
#             current_energy -= 30
#             coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             current_energy += 50
#             print("You had to rest!")
#     else:
#         ingredient = current_event[0]
#         if coins >= event_value:
#             coins -= event_value
#             print(f"You bought {ingredient}.")
#         else:
#             cannot_afford_ingredient = True
#             print(f"Closed! Cannot afford {ingredient}.")
#             break
#
# else:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {current_energy}")