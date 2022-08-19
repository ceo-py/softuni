liked_meals = {}
unliked_meals = 0


def liked_meal(guest, meal):
    liked_meals[guest] = liked_meals.get(guest, [])
    if meal not in liked_meals[guest]:
        liked_meals[guest].append(meal)


def disliked_meal(guest, meal):
    global unliked_meals
    if guest not in liked_meals:
        print(f"{guest} is not at the party.")
    elif meal not in liked_meals[guest]:
        print(f"{guest} doesn't have the {meal} in his/her collection.")
    elif meal in liked_meals[guest]:
        liked_meals[guest].remove(meal)
        unliked_meals += 1
        print(f"{guest} doesn't like the {meal}.")


def show_result():
    if liked_meals:
        for guest in liked_meals:
            print(f"{guest}: {', '.join(liked_meals[guest])}")
    print(f"Unliked meals: {unliked_meals}")


command_func = {
    "Like": liked_meal,
    "Dislike": disliked_meal
}

command = input()

while command != "Stop":
    command_type, guest, meal = command.split("-")
    command_func[command_type](guest, meal)
    command = input()

show_result()