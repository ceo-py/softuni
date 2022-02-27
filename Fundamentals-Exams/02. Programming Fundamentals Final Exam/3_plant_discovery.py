total_plants = int(input())

plant_info = {}
total_rating = "total"
rating_plant = "rating"
rarity_d = "rarity"
resul_list = []
for _ in range(total_plants):
    command = input().split("<->")
    plant_name = command[0]
    plant_rarity = int(command[1])
    if plant_name not in plant_info:
        plant_info[plant_name] = {}
        plant_info[plant_name][total_rating] = 0
        plant_info[plant_name][rating_plant] = 0
    plant_info[plant_name][rarity_d] = plant_rarity


def reset_plant(name):
    if name in plant_info:
        plant_info[name][total_rating] = 0
        plant_info[name][rating_plant] = 0
    else:
        print("error")


def rate_plant(name, rating):
    if name in plant_info:
        plant_info[name][total_rating] += rating
        plant_info[name][rating_plant] += 1
    else:
        print("error")


def update_plant(name, rating):
    if name in plant_info:
        plant_info[name][rarity_d] = rating
    else:
        print("error")


def show_result():
    print(f"Plants for the exhibition:")
    name_d = "name"
    for name in plant_info:
        zero_rating = True
        for key, value in plant_info[name].items():
            if key == "total":
                if value > 0:
                    total_rt = value
                    zero_rating = False
            elif key == "rating" and not zero_rating:
                number_added = value
            elif key == "rarity":
                rarity_enter = value
        if not zero_rating:
            resul_list.append({name_d: name, rating_plant: total_rt / number_added, rarity_d: rarity_enter})
        else:
            resul_list.append({name_d: name, rating_plant: 0.00, rarity_d: rarity_enter})
    resul_list.sort(key=lambda item: (-item[rarity_d], -item[rating_plant]))
    for show in resul_list:
        print(f"- {show[name_d]}; Rarity: {show[rarity_d]}; Rating: {(show[rating_plant]):.2f}")


command = input()

while command != "Exhibition":
    if "Reset" in command:
        command = command.replace("Reset: ", "")
        reset_plant(command)
    elif "Rate" in command:
        command = (command.replace("Rate: ", "")).split(" - ")
        name = command[0]
        rating = int(command[1])
        rate_plant(name, rating)
    elif "Update" in command:
        command = (command.replace("Update: ", "")).split(" - ")
        name = command[0]
        rating = int(command[1])
        update_plant(name, rating)

    command = input()

show_result()
