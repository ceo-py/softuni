number_cars = int(input())
parking_info = {}


def register_car(name, number):
    if name in parking_info:
        print(f"ERROR: already registered with plate number {parking_info[name]}")
        return
    parking_info[name] = number
    print(f"{name} registered {number} successfully")


def unregister_car(name):
    if name not in parking_info:
        print(f"ERROR: user {name} not found")
        return
    del parking_info[name]
    print(f"{name} unregistered successfully")


def all_cars_in_praking():
    for key, value in parking_info.items():
        print(f"{key} => {value}")


for _ in range(number_cars):
    command, name, *number = input().split()
    if command == "register":
        number = number[-1]
        register_car(name, number)
    else:
        unregister_car(name)

all_cars_in_praking()



#
#
# number_cars = int(input())
# parking_info = {}
#
#
# def register_car(name, number):
#     if name in parking_info:
#         print(f"ERROR: already registered with plate number {parking_info[name]}")
#     else:
#         parking_info[name] = number
#         print(f"{name} registered {number} successfully")
#
#
# def unregister_car(name):
#     if name not in parking_info:
#         print(f"ERROR: user {name} not found")
#     else:
#         del parking_info[name]
#         print(f"{name} unregistered successfully")
#
#
# def all_cars_in_praking():
#     for key, value in parking_info.items():
#         print(f"{key} => {value}")
#
#
# for _ in range(number_cars):
#     car = input()
#     car = car.split()
#     command = car[0]
#     name = car[1]
#     if command == "register":
#         number = car[-1]
#         register_car(name, number)
#     else:
#         unregister_car(name)
#
# all_cars_in_praking()
