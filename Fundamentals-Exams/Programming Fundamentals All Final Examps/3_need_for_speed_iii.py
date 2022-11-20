number_of_cars = int(input())

cars_info = {}

for car in range(number_of_cars):
    car_name, *info = (int(x) if x.isdigit() else x for x in input().split("|"))
    cars_info[car_name] = info


def drive(info):
    car_name, distance, fuel = info
    if cars_info[car_name][1] >= fuel:
        cars_info[car_name][1] -= fuel
        cars_info[car_name][0] += distance
        print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_info[car_name][0] >= 100_000:
            del cars_info[car_name]
            print(f"Time to sell the {car_name}!")
    else:
        print("Not enough fuel to make that ride")


def refuel(info):
    car_name, fuel = info
    if cars_info[car_name][1] + fuel > 75:
        fuel = 75 - cars_info[car_name][1]
    cars_info[car_name][1] += fuel
    print(f"{car_name} refueled with {fuel} liters")


def revert(info):
    car_name, kilometers = info
    cars_info[car_name][0] -= kilometers
    if cars_info[car_name][0] < 10_000:
        cars_info[car_name][0] = 10_000
    else:
        print(f"{car_name} mileage decreased by {kilometers} kilometers")


def show_result():
    for car in cars_info:
        print(f"{car} -> Mileage: {cars_info[car][0]} kms, Fuel in the tank: {cars_info[car][1]} lt.")


command_func = {
    "Drive": drive,
    "Refuel": refuel,
    "Revert": revert
}

command = input()
while command != "Stop":
    command_type, *info = (int(x) if x.isdigit() else x for x in command.split(" : "))
    command_func[command_type](info)
    command = input()

show_result()



#
# car_numbers = int(input())
#
# car_info = {}
#
#
# class Car:
#
#     def __init__(self, name):
#         self.name = name
#         self.mileage = 0
#         self.fuel = 0
#
#     def add_mileage(self, mileage):
#         self.mileage += mileage
#
#     def add_fuel(self, fuel):
#         self.fuel += fuel
#
#     def drive(self, distance, fuel):
#         if self.fuel > fuel:
#             self.fuel -= fuel
#             self.mileage += distance
#             print(f"{self.name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             if self.mileage >= 100_000:
#                 del car_info[self.name]
#                 print(f"Time to sell the {self.name}!")
#         else:
#             print("Not enough fuel to make that ride")
#
#     def refuel(self, fuel):
#         if self.fuel + fuel > 75:
#             fuel = 75 - self.fuel
#         self.fuel += fuel
#         print(f"{self.name} refueled with {fuel} liters")
#
#     def revert(self, kilometers):
#         self.mileage -= kilometers
#         if self.mileage < 10_000:
#             self.mileage = 10_000
#             return
#         print(f"{self.name} mileage decreased by {kilometers} kilometers")
#
#     def __repr__(self):
#         return f"{self.name} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."
#
#
# for car in range(car_numbers):
#     car_name, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
#     car_info[car_name] = car_info.get(car_name, Car(car_name))
#     car_info[car_name].add_mileage(mileage)
#     car_info[car_name].add_fuel(fuel)
#
#
# command = input()
#
# while command != "Stop":
#     command_type, car_name, *info = [int(x) if x.isdigit() else x for x in command.split(" : ")]
#     if command_type == "Drive":
#         distance, fuel = info
#         car_info[car_name].drive(distance, fuel)
#     elif command_type == "Refuel":
#         fuel = info[0]
#         car_info[car_name].refuel(fuel)
#     elif command_type == "Revert":
#         kilometers = info[0]
#         car_info[car_name].revert(kilometers)
#     command = input()
#
# for car in car_info.values():
#     print(car)
#
#
#



#
# number_of_cars = int(input())
#
#
# cars_info = {}
#
# for car in range(number_of_cars):
#     car_name, car_mileage, car_fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
#     cars_info[car_name] = cars_info.get(car_name, {})
#     cars_info[car_name]["Mileage"] = car_mileage
#     cars_info[car_name]["Fuel"] = car_fuel
#
#
# def drive_car(car_name, car_distance, car_fuel):
#     if cars_info[car_name]["Fuel"] < car_fuel:
#         print("Not enough fuel to make that ride")
#     else:
#         cars_info[car_name]["Fuel"] -= car_fuel
#         cars_info[car_name]["Mileage"] += car_distance
#         print(f"{car_name} driven for {car_distance} kilometers. {car_fuel} liters of fuel consumed.")
#         if cars_info[car_name]["Mileage"] >= 100_000:
#             del cars_info[car_name]
#             print(f"Time to sell the {car_name}!")
#
#
# def refuel_car(car_name, car_fuel):
#     if cars_info[car_name]["Fuel"] + car_fuel > 75:
#         car_fuel = 75 - cars_info[car_name]["Fuel"]
#         cars_info[car_name]["Fuel"] = 75
#     else:
#         cars_info[car_name]["Fuel"] += car_fuel
#     print(f"{car_name} refueled with {car_fuel} liters")
#
#
# def revert_car(car_name, car_kilometers):
#     if cars_info[car_name]["Mileage"] - car_kilometers < 10_000:
#         cars_info[car_name]["Mileage"] = 10_000
#     else:
#         cars_info[car_name]["Mileage"] -= car_kilometers
#         print(f"{car_name} mileage decreased by {car_kilometers} kilometers")
#
#
# def show_result():
#     for car_name in cars_info:
#         print(f"{car_name} -> Mileage: {cars_info[car_name]['Mileage']} kms,"
#               f" Fuel in the tank: {cars_info[car_name]['Fuel']} lt.")
#
#
# command = input()
# while command != "Stop":
#     command_type, *others = [int(x) if x.isdigit() else x for x in command.split(" : ")]
#     if "Drive" == command_type:
#         car_name, car_mileage, car_fuel = others
#         drive_car(car_name, car_mileage, car_fuel)
#     else:
#         car_name, fuel_or_kilometers = others
#         if "Refuel" == command_type:
#             refuel_car(car_name, fuel_or_kilometers)
#         elif "Revert" == command_type:
#             revert_car(car_name, fuel_or_kilometers)
#     command = input()
#
# show_result()
#
#
#






#
#
# number_cards = int(input())
# car_d = "car"
# distance_d = "distance"
# fuel_d = "fuel"
# car_info = {}
# car_list = []
#
#
# def drive_car(name, distance, fuel):
#     if car_info[name][fuel_d] >= fuel:
#         car_info[name][fuel_d] += - fuel
#         car_info[name][distance_d] += distance
#         print(f"{name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#         if car_info[name][distance_d] >= 100_000:
#             del car_info[name]
#             print(f"Time to sell the {name}!")
#     else:
#         print("Not enough fuel to make that ride")
#
#
# def refuel_car(name, fuel):
#     fill_liters = False
#     litters = 0
#     for _ in range(fuel):
#         if car_info[name][fuel_d] < 75:
#             car_info[name][fuel_d] += 1
#             litters += 1
#             fill_liters = True
#         else:
#             break
#
#     if fill_liters:
#         print(f"{name} refueled with {litters} liters")
#
#
# def revert_car(name, kilometers):
#     under_ten = False
#     car_info[name][distance_d] += - kilometers
#     if car_info[name][distance_d] < 10_000:
#         car_info[name][distance_d] = 10_000
#         under_ten = True
#     if not under_ten:
#         print(f"{name} mileage decreased by {kilometers} kilometers")
#
#
# def adding_cars(number):
#     for _ in range(number):
#         car = input().split("|")
#         car_name = car[0]
#         car_distance = int(car[1])
#         car_fuel = int(car[-1])
#         if car_name not in car_info:
#             car_info[car_name] = {}
#         car_info[car_name][distance_d] = car_distance
#         car_info[car_name][fuel_d] = car_fuel
#
#
# def show_result():
#     for car in car_info:
#         car_list.append({car_d: car, distance_d: car_info[car][distance_d], fuel_d: car_info[car][fuel_d]})
#     car_list.sort(key=lambda item: (-item[distance_d], item[car_d]))
#     for show in car_list:
#         print(f"{show[car_d]} -> Mileage: {show[distance_d]} kms, Fuel in the tank: {show[fuel_d]} lt.")
#
#
# adding_cars(number_cards)
# command = input()
#
# while command != "Stop":
#     command = command.split(" : ")
#     car_command = command[0]
#     car_name = command[1]
#     car_distance = int(command[2])
#     if car_command == "Drive":
#         car_fuel = int(command[-1])
#         drive_car(car_name, car_distance, car_fuel)
#     elif car_command == "Refuel":
#         refuel_car(car_name, car_distance)
#     elif car_command == "Revert":
#         revert_car(car_name, car_distance)
#     command = input()
#
# show_result()
