from collections import deque


class WaterDispenser:
    quantity = 0
    water_line = deque()

    def add_person_to_q(self, name: str):
        self.water_line.append(name)

    def refill(self, litters: int):
        self.quantity += litters

    def get_water(self, litters: int):
        if litters <= self.quantity:
            self.quantity -= litters
            return f"{self.water_line.popleft()} got water"
        return f"{self.water_line.popleft()} must wait"


dispenser = WaterDispenser()

dispenser.quantity = int(input())
person = input()

while person != "Start":
    dispenser.add_person_to_q(person)
    person = input()

command = input()
while command != "End":
    if command.isdigit():
        print(dispenser.get_water(int(command)))
    else:
        _, litters_to_refill = command.split()
        dispenser.refill(int(litters_to_refill))
    command = input()

print(f"{dispenser.quantity} liters left")






# from collections import deque
#
# dispenser_quantity = int(input())
# person = input()
#
# water_line = deque()
#
#
# def refill(liters):
#     global dispenser_quantity
#     dispenser_quantity += liters
#
#
# def get_water(liters):
#     global dispenser_quantity
#     if liters <= dispenser_quantity:
#         dispenser_quantity -= liters
#         print(f"{water_line.popleft()} got water")
#     else:
#         print(f"{water_line.popleft()} must wait")
#
#
# while person != "Start":
#     water_line.append(person)
#     person = input()
#
# command = input()
# while command != "End":
#     if command.isdigit():
#         get_water(int(command))
#     else:
#         _, litters_to_refill = command.split()
#         refill(int(litters_to_refill))
#     command = input()
#
# print(f"{dispenser_quantity} liters left")




# quantity = int(input())
#
# people_in_q = []
# people_litters_drink = []
# data_input = input()
# while data_input != "Start":
#     people_in_q.append(data_input)
#     data_input = input()
#
# data_input = input()
# while data_input != "End":
#     if "refill" in data_input:
#         quantity += int(data_input.split()[-1])
#         data_input = input()
#         continue
#     people_litters_drink.append(int(data_input))
#     data_input = input()
#
# for name, liters in zip(people_in_q.copy(), people_litters_drink.copy()):
#     if quantity - liters >= 0:
#         quantity -= liters
#         print(f"{name} got water")
#         people_in_q.pop(0)
#     else:
#         print(f"{name} must wait")
#
# print(f"{quantity} liters left")
