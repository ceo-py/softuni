number_rooms = int(input())

enough_chairs = True
chairs_left = 0


def check_chairs(chairs, people, room_floor):
    if chairs < people:
        result = people - chairs
        global enough_chairs
        enough_chairs = False
        return print(f"{result} more chairs needed in room {room_floor}")
    elif chairs >= people:
        global chairs_left
        chairs_left += chairs - people


for room in range(1, number_rooms + 1):
    command = input().split()
    check_chairs(len(command[0]), int(command[1]), room)


if enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
