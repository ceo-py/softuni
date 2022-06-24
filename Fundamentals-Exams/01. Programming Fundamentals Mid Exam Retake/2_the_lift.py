passengers = int(input())
floors = [int(n) for n in input().split()]
floors_lift = list()
enough_spots = True
total = passengers
equal_spots = True


def check_floors():
    global passengers
    global total
    for floor in floors:
        for i in range(4):
            if passengers > 0:
                if floor + 1 <= 4:
                    floor += 1
                    passengers += - 1
        floors_lift.append(floor)


check_floors()
max_people = (len(floors_lift) * 4) - sum(floors)
if max_people == total:
    equal_spots = False

elif passengers != 0:
    enough_spots = False

if enough_spots and equal_spots:
    print("The lift has empty spots!")

if not enough_spots and equal_spots:
    print(f"There isn't enough space! {passengers} people in a queue!")

print(*floors_lift, sep=" ")




#
# people = int(input())
# current_wagons = list(map(int, input().split()))
# for i in range(len(current_wagons)):
#     max_people = min(4 - current_wagons[i], people)
#     current_wagons[i] += max_people
#     people -= max_people
#
# if people > 0:
#     print(f"There isn't enough space! {people} people in a queue!")
# elif len([wagon for wagon in current_wagons if wagon < 4]) > 0:
#     print("The lift has empty spots!")
#
# print(" ".join([str(wagon) for wagon in current_wagons]))
