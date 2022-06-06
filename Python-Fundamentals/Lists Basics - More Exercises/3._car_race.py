sequence_of_numbers = [int(num) for num in input().split()]

first_car = len(sequence_of_numbers) // 2

first_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[:first_car][:pos]) * 0.2 for pos, num in
                       enumerate(sequence_of_numbers[:first_car])])
second_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[::-1][:first_car][:pos]) * 0.2 for pos, num in
                    enumerate(sequence_of_numbers[::-1][:first_car])])

if first_car_score < second_car_score:
    print(f"The winner is left with total time: {first_car_score:.1f}")
else:
    print(f"The winner is right with total time: {second_car_score:.1f}")



#
# sequence_of_numbers = input().split(" ")
#
# car_one_total = 0
# car_two_total = 0
# s_car = sequence_of_numbers
# where_is_split = len(sequence_of_numbers) // 2
#
# for car_one, car_two in zip(sequence_of_numbers[:where_is_split], s_car[::-1]):
#     car_one = int(car_one)
#     car_two = int(car_two)
#     if car_one == 0:
#         car_one_total = car_one_total * 0.8
#     else:
#         car_one_total += car_one
#
#     if car_two == 0:
#         car_two_total = car_two_total * 0.8
#     else:
#         car_two_total += car_two
#
# if car_one_total < car_two_total:
#     print(f"The winner is left with total time: {car_one_total:.1f}")
#
# else:
#     print(f"The winner is right with total time: {car_two_total:.1f}")
#
#



# sequence_of_numbers = input().split(" ")
#
# first_car = list()
# second_car = list()
# car_one_total = 0
# car_two_total = 0
#
# where_is_split = len(sequence_of_numbers) // 2
# for car_one in sequence_of_numbers[:where_is_split]:
#     first_car.append(float(car_one))
#
# sequence_of_numbers.reverse()
# for car_two in sequence_of_numbers[:where_is_split]:
#     second_car.append(float(car_two))
#
# for one, two in zip(first_car, second_car):
#     if one == 0:
#         car_one_total = car_one_total * 0.8
#     else:
#         car_one_total += one
#
#     if two == 0:
#         car_two_total = car_two_total * 0.8
#     else:
#         car_two_total += two
#
# if car_one_total < car_two_total:
#     print(f"The winner is left with total time: {car_one_total:.1f}")
#
# else:
#     print(f"The winner is right with total time: {car_two_total:.1f}")
