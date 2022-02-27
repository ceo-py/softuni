count_load = int(input())

minibus = 0
truck = 0
train = 0
total_load = 0
tons = 0
minibus_tons = 0
truck_tons = 0
train_tons = 0

for _ in range(1, count_load + 1):
    load = int(input())
    tons += load

    if load <= 3:
        minibus += + load * 200
        minibus_tons += load

    elif load <= 11:
        truck += + load * 175
        truck_tons += load

    elif load > 11:
        train += + load * 120
        train_tons += load

total_load = minibus + truck + train
average_per_ton = total_load / tons
average_per_ton_minibus = (minibus_tons / tons) * 100
average_per_ton_truck = (truck_tons / tons) * 100
average_per_ton_train = (train_tons / tons) * 100
print(
    f"{average_per_ton:.2f}\n{average_per_ton_minibus:.2f}%\n{average_per_ton_truck:.2f}%\n{average_per_ton_train:.2f}%")
