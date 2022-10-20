from collections import deque

seats = input().split(", ")
first_number = deque(int(x) for x in input().split(", "))
second_number = deque(int(x) for x in input().split(", "))

rotations, matched_seats = 0, []

while len(matched_seats) != 3 and rotations != 10:
    first_num = first_number.popleft()
    second_num = second_number.pop()
    rotations += 1

    letter = chr(first_num + second_num)
    found = False
    for seat in (f"{first_num}{letter}", f"{second_num}{letter}"):
        if seat in seats:
            matched_seats.append(seat)
            seats.remove(seat)
            found = True

    if found:
        continue

    first_number.append(first_num)
    second_number.appendleft(second_num)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")


















#
#
#
# from collections import deque
#
# seats = input().split(", ")
# first_matching_seats = deque(int(x) for x in input().split(", "))
# second_matching_seats = deque(int(x) for x in input().split(", "))
# rotations, found_seat_matches = 0, []
#
#
# while rotations < 10:
#     rotations += 1
#     first_num = first_matching_seats.popleft()
#     second_num = second_matching_seats.pop()
#     found_seat, letter = False, chr(first_num + second_num)
#     for seat in [f"{first_num}{letter}", f"{second_num}{letter}"]:
#         if seat in seats:
#             seats.remove(seat)
#             found_seat_matches.append(seat)
#             found_seat = True
#     if len(found_seat_matches) == 3:
#         break
#     if not found_seat:
#         first_matching_seats.append(first_num)
#         second_matching_seats.appendleft(second_num)
#
# print(f"Seat matches: {', '.join(found_seat_matches)}")
# print(f"Rotations count: {rotations}")
#
#
# '''
# Seat matches: 25A, 44F
# Rotations count: 10'''
#
#
