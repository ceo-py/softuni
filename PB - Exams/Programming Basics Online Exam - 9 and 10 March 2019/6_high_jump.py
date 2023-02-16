target_high_jump = int(input())

current_high_jump = target_high_jump - 30
unsuccessful_jumps = 0
jumps_counter = 0

while unsuccessful_jumps < 3:
    jump = int(input())

    jumps_counter += 1

    if jump > current_high_jump:
        unsuccessful_jumps = 0
        current_high_jump += 5

        if current_high_jump > target_high_jump:
            print(f"Tihomir succeeded, he jumped over {target_high_jump}cm after {jumps_counter} jumps.")
            break

    else:
        unsuccessful_jumps += 1

else:
    print(f"Tihomir failed at {current_high_jump}cm after {jumps_counter} jumps.")






#
#
#
# target_jump = int(input())
#
# total_jumps = 0
# unsuccessful_jump_counter = 0
# first_target_jump = target_jump - 30
#
# while True:
#     jump = int(input())
#     total_jumps += 1
#
#     if jump > target_jump and first_target_jump >= target_jump:
#         print(f"Tihomir succeeded, he jumped over {first_target_jump}cm after {total_jumps} jumps.")
#         break
#
#     elif jump > first_target_jump:
#         first_target_jump += 5
#         unsuccessful_jump_counter = 0
#
#     else:
#         unsuccessful_jump_counter += 1
#
#     if unsuccessful_jump_counter == 3:
#         print(f"Tihomir failed at {first_target_jump}cm after {total_jumps} jumps.")
#         break


#
#
# goal_high = int(input())
# first_high = goal_high - 30
#
# jump = 0
# no_jump = 0
#
# while no_jump < 3:
#     high = int(input())
#     jump += 1
#     if high > first_high:
#         no_jump = 0
#         first_high += 5
#     else:
#         no_jump += 1
#
#     if first_high > goal_high:
#         print(f'Tihomir succeeded, he jumped over {goal_high}cm after {jump} jumps.')
#         exit()
#
# print(f'Tihomir failed at {first_high}cm after {jump} jumps.')
#
