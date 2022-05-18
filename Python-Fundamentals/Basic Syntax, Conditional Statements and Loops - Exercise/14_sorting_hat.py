name = input()
going_to = {
    "Gryffindor": 5,
    "Slytherin": 6,
    "Ravenclaw": 7,
    "Hufflepuff": 100
}

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for destination, num in going_to.items():
        if len(name) < num:
            print(f"{name} goes to {destination}.")
            break
    name = input()
else:
    print("Welcome to Hogwarts.")
