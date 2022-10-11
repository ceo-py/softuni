neighborhood = [int(x) for x in input().split("@")]
jump_data = input()
neighborhood_len = len(neighborhood)
length = 0

while jump_data != "Love!":
    length += int(jump_data.split()[-1])
    if length >= neighborhood_len:
        length = 0

    if neighborhood[length] > 2:
        neighborhood[length] -= 2
    else:
        if neighborhood[length] != 0:
            neighborhood[length] -= 2
            text = "has"
        else:
            text = "already had"
        print(f"Place {length} {text} Valentine's day.")
    jump_data = input()

print(f"Cupid's last position was {length}.")

failed_houses = sum(1 for x in neighborhood if x != 0)

if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")



#
# neighborhood = [int(n) for n in input().split("@")]
#
# jump_command = input()
# jump_position = 0
#
#
# def jump_neighborhood(length_d):
#     global jump_position
#     jump_position += length_d
#     if jump_position >= len(neighborhood):
#         jump_position = 0
#     if neighborhood[jump_position] == 0:
#         print(f"Place {jump_position} already had Valentine's day.")
#     else:
#         neighborhood[jump_position] -= 2
#         if neighborhood[jump_position] == 0:
#             print(f"Place {jump_position} has Valentine's day.")
#
#
# while jump_command != "Love!":
#     jump_command = jump_command.split()
#     jump_neighborhood(int(jump_command[1]))
#
#     jump_command = input()
#
# print(f"Cupid's last position was {jump_position}.")
#
# if sum(neighborhood) == 0:
#     print("Mission was successful.")
# else:
#     fail_count = neighborhood.count(0)
#     print(f"Cupid has failed {len(neighborhood) - fail_count} places.")
