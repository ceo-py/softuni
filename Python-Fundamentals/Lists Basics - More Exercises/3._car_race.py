sequence_of_numbers = input().split(" ")

first_car = list()
second_car = list()
car_one_total = 0
car_two_total = 0

where_is_split = len(sequence_of_numbers) // 2
for car_one in sequence_of_numbers[:where_is_split]:
    first_car.append(float(car_one))

sequence_of_numbers.reverse()
for car_two in sequence_of_numbers[:where_is_split]:
    second_car.append(float(car_two))

for one, two in zip(first_car, second_car):
    if one == 0:
        car_one_total = car_one_total * 0.8
    else:
        car_one_total += one

    if two == 0:
        car_two_total = car_two_total * 0.8
    else:
        car_two_total += two

if car_one_total < car_two_total:
    print(f"The winner is left with total time: {car_one_total:.1f}")

else:
    print(f"The winner is right with total time: {car_two_total:.1f}")
