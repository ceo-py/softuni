number_of_plants = int(input())

plants_info = {}

for plant in range(number_of_plants):
    plant_name, rarity = input().split("<->")
    plants_info[plant_name] = [rarity, []]


def check_plant_exist(plant):
    if plant in plants_info:
        return True
    print("error")


def rate(info):
    plant, rating = info.split(" - ")
    plants_info[plant][1].append(int(rating))


def update(info):
    plant, new_rarity = info.split(" - ")
    plants_info[plant][0] = new_rarity


def reset(info):
    plant = info
    plants_info[plant][1] = []


def show_result():
    print("Plants for the exhibition:")
    for plant in plants_info:
        average_rating = 0
        if sum(plants_info[plant][1]) != 0:
            average_rating = sum(plants_info[plant][1]) / len(plants_info[plant][1])
        print(f"- {plant}; Rarity: {plants_info[plant][0]}; Rating: {average_rating:.2f}")


command_func = {
    "Rate": rate,
    "Update": update,
    "Reset": reset
}

command = input()
while command != "Exhibition":
    command_type, info = command.split(": ")
    if check_plant_exist(info.split(" - ")[0]):
        command_func[command_type](info)
    command = input()

show_result()







#
# number_of_pants = int(input())
#
# plant_info = {}
# rarity_d, rating_d = "Rarity", "Rating"
# for plant in range(number_of_pants):
#     plant_name, plant_rarity = input().split("<->")
#     plant_info[plant_name] = plant_info.get(plant_name, {})
#     plant_info[plant_name][rarity_d] = float(plant_rarity)
#     plant_info[plant_name][rating_d] = []
#
#
# def check_plant_name(plant_name):
#     if plant_name not in plant_info:
#         print("error")
#         return
#     return True
#
#
# def rate_plant(plant_name, plant_rating):
#     if check_plant_name(plant_name):
#         plant_info[plant_name][rating_d].append(plant_rating)
#
#
# def update_plant(plant_name, new_rarity):
#     if check_plant_name(plant_name):
#         plant_info[plant_name][rarity_d] = new_rarity
#
#
# def reset_plant(plant_name):
#     if check_plant_name(plant_name):
#         plant_info[plant_name][rating_d] = []
#
#
# def show_result():
#     print("Plants for the exhibition:")
#     for plant in plant_info:
#         average = 0.00
#         if sum(plant_info[plant][rating_d]) != 0:
#             average = sum(plant_info[plant][rating_d]) / len(plant_info[plant][rating_d])
#         print(
#             f"- {plant}; Rarity: {plant_info[plant][rarity_d]:.0f}; Rating: {average:.2f}")
#
#
# command = input()
#
# while command != "Exhibition":
#     if "Reset" in command:
#         _, plant_name = command.split(": ")
#         reset_plant(plant_name)
#         command = input()
#         continue
#     plant_name, rating_or_rarity = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]
#     if "Rate" in command:
#         rate_plant(plant_name, rating_or_rarity)
#     elif "Update" in command:
#         update_plant(plant_name, rating_or_rarity)
#     command = input()
#
# show_result()
#
#



#
#
# total_plants = int(input())
#
# plant_info = {}
# total_rating = "total"
# rating_plant = "rating"
# rarity_d = "rarity"
# resul_list = []
# for _ in range(total_plants):
#     command = input().split("<->")
#     plant_name = command[0]
#     plant_rarity = int(command[1])
#     if plant_name not in plant_info:
#         plant_info[plant_name] = {}
#         plant_info[plant_name][total_rating] = 0
#         plant_info[plant_name][rating_plant] = 0
#     plant_info[plant_name][rarity_d] = plant_rarity
#
#
# def reset_plant(name):
#     if name in plant_info:
#         plant_info[name][total_rating] = 0
#         plant_info[name][rating_plant] = 0
#     else:
#         print("error")
#
#
# def rate_plant(name, rating):
#     if name in plant_info:
#         plant_info[name][total_rating] += rating
#         plant_info[name][rating_plant] += 1
#     else:
#         print("error")
#
#
# def update_plant(name, rating):
#     if name in plant_info:
#         plant_info[name][rarity_d] = rating
#     else:
#         print("error")
#
#
# def show_result():
#     print(f"Plants for the exhibition:")
#     name_d = "name"
#     for name in plant_info:
#         zero_rating = True
#         for key, value in plant_info[name].items():
#             if key == "total":
#                 if value > 0:
#                     total_rt = value
#                     zero_rating = False
#             elif key == "rating" and not zero_rating:
#                 number_added = value
#             elif key == "rarity":
#                 rarity_enter = value
#         if not zero_rating:
#             resul_list.append({name_d: name, rating_plant: total_rt / number_added, rarity_d: rarity_enter})
#         else:
#             resul_list.append({name_d: name, rating_plant: 0.00, rarity_d: rarity_enter})
#     resul_list.sort(key=lambda item: (-item[rarity_d], -item[rating_plant]))
#     for show in resul_list:
#         print(f"- {show[name_d]}; Rarity: {show[rarity_d]}; Rating: {(show[rating_plant]):.2f}")
#
#
# command = input()
#
# while command != "Exhibition":
#     if "Reset" in command:
#         command = command.replace("Reset: ", "")
#         reset_plant(command)
#     elif "Rate" in command:
#         command = (command.replace("Rate: ", "")).split(" - ")
#         name = command[0]
#         rating = int(command[1])
#         rate_plant(name, rating)
#     elif "Update" in command:
#         command = (command.replace("Update: ", "")).split(" - ")
#         name = command[0]
#         rating = int(command[1])
#         update_plant(name, rating)
#
#     command = input()
#
# show_result()
