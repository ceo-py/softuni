items_accessories = input().split("|")

energy = 100
coins = 100

for clean_text in items_accessories:
    if "rest-" in clean_text:
        text = int(clean_text.replace("rest-", ""))
        energy += text
        if energy < 100:
            energy += text
            print(f"You gained {text} energy.")
        else:
            diffrence = (energy - text) - (energy - text)
            energy += - text
            print(f"You gained {diffrence} energy.")
        print(f"Current energy: {energy}.")


    elif "order-" in clean_text:
        text = int(clean_text.replace("order-", ""))
        if energy > text - 30:
            print(f"You earned {text} coins.")
            energy += - 30
        else:
            energy += 50
            print(f"You had to rest!")


    else:
        text = clean_text.split("-")
        number = int(text[-1])
        text = text[0]
        if coins - number >= 0:
            coins += - number
            print(f"You bought {text}")
        else:
            print(f"Closed! Cannot afford {text}.")
