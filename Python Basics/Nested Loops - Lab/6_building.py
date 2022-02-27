building_floors = int(input())
rooms_per_floors = int(input())

for floors in range(building_floors, 0, - 1):
    for rooms in range(rooms_per_floors):
        if floors == building_floors:
            print(f"L{floors}{rooms}", end=" ")
        else:
            if floors % 2 != 0:
                print(f"A{floors}{rooms}", end=" ")
            else:
                print(f"O{floors}{rooms}", end=" ")
    print("")
