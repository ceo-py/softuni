def accommodate(*args, **kwargs):
    sorted_rooms = dict(sorted(kwargs.items(), key=lambda x: (x[1], x[0])))
    hotel = {
        "accommodated": {},
        "unaccommodated": {},
    }
    for group in args:
        for room, room_size in sorted_rooms.items():
            if room_size >= group:
                hotel["accommodated"][room] = group
                del sorted_rooms[room]
                break
        else:
            hotel["unaccommodated"][group] = room_size
    output = []

    if not hotel["accommodated"]:
        output.append("No accommodations were completed!")

    elif hotel["accommodated"]:
        output.append(f"A total of {len(hotel['accommodated'])} accommodations were completed!")
        output += [f"<Room {room.replace('room_', '')} accommodates {room_size} guests>" for room,
        room_size in sorted(hotel['accommodated'].items(), key=lambda x: x[0])]
    if hotel["unaccommodated"]:
        output.append(f"Guests with no accommodation: {sum(args) - sum(hotel['accommodated'].values())}")
    if sorted_rooms:
        output.append(f"Empty rooms: {len(sorted_rooms)}")

    return "\n".join(output)

# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print()

# print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print()

# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
