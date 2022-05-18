main_events = input().split("|")

energy = 100
coins = 100


def rest_event(energy_number):
    global energy
    if energy + energy_number > 100:
        print(f"You gained {abs(100 - energy)} energy.")
        energy = 100
    else:
        energy += energy_number
        print(f"You gained {energy_number} energy.")
    print(f"Current energy: {energy}.")


def order_event(coins_number):
    global energy, coins
    if energy - 30 >= 0:
        coins += coins_number
        energy -= 30
        print(f"You earned {coins_number} coins.")
    else:
        print("You had to rest!")
        energy += 50


def ingredient_event(name, price_item):
    global coins
    if price_item <= coins:
        print(f"You bought {name}.")
        coins -= price_item
    else:
        print(f"Closed! Cannot afford {name}.")
        exit()


for event_type in main_events:
    event_type = event_type.split("-")
    event_command = event_type[0]
    event_energy_coins = int(event_type[-1])

    if event_command == "rest":
        rest_event(event_energy_coins)
    elif event_command == "order":
        order_event(event_energy_coins)
    else:
        ingredient_event(event_command, event_energy_coins)

print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
