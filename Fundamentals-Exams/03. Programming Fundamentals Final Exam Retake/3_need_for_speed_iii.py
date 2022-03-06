number_cards = int(input())
car_d = "car"
distance_d = "distance"
fuel_d = "fuel"
car_info = {}
car_list = []


def drive_car(name, distance, fuel):
    if car_info[name][fuel_d] >= fuel:
        car_info[name][fuel_d] += - fuel
        car_info[name][distance_d] += distance
        print(f"{name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_info[name][distance_d] >= 100_000:
            del car_info[name]
            print(f"Time to sell the {name}!")
    else:
        print("Not enough fuel to make that ride")


def refuel_car(name, fuel):
    fill_liters = False
    litters = 0
    for _ in range(fuel):
        if car_info[name][fuel_d] < 75:
            car_info[name][fuel_d] += 1
            litters += 1
            fill_liters = True
        else:
            break

    if fill_liters:
        print(f"{name} refueled with {litters} liters")


def revert_car(name, kilometers):
    under_ten = False
    car_info[name][distance_d] += - kilometers
    if car_info[name][distance_d] < 10_000:
        car_info[name][distance_d] = 10_000
        under_ten = True
    if not under_ten:
        print(f"{name} mileage decreased by {kilometers} kilometers")


def adding_cars(number):
    for _ in range(number):
        car = input().split("|")
        car_name = car[0]
        car_distance = int(car[1])
        car_fuel = int(car[-1])
        if car_name not in car_info:
            car_info[car_name] = {}
        car_info[car_name][distance_d] = car_distance
        car_info[car_name][fuel_d] = car_fuel


def show_result():
    for car in car_info:
        car_list.append({car_d: car, distance_d: car_info[car][distance_d], fuel_d: car_info[car][fuel_d]})
    car_list.sort(key=lambda item: (-item[distance_d], item[car_d]))
    for show in car_list:
        print(f"{show[car_d]} -> Mileage: {show[distance_d]} kms, Fuel in the tank: {show[fuel_d]} lt.")


adding_cars(number_cards)
command = input()

while command != "Stop":
    command = command.split(" : ")
    car_command = command[0]
    car_name = command[1]
    car_distance = int(command[2])
    if car_command == "Drive":
        car_fuel = int(command[-1])
        drive_car(car_name, car_distance, car_fuel)
    elif car_command == "Refuel":
        refuel_car(car_name, car_distance)
    elif car_command == "Revert":
        revert_car(car_name, car_distance)
    command = input()

show_result()
