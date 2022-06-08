car_numbers = int(input())

parking_lot = {}
for car in range(car_numbers):
    direction, car_plate_number = input().split(", ")
    if "IN" == direction:
        parking_lot[car_plate_number] = direction
        continue
    del parking_lot[car_plate_number]

if parking_lot.keys():
    print('\n'.join(parking_lot.keys()))
else:
    print("Parking Lot is Empty")