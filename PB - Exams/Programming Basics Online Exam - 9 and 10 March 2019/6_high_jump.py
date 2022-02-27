target_jump = int(input())

total_jumps = 0
unsuccessful_jump_counter = 0
first_target_jump = target_jump - 30

while True:
    jump = int(input())
    total_jumps += 1

    if jump > target_jump and first_target_jump >= target_jump:
        print(f"Tihomir succeeded, he jumped over {first_target_jump}cm after {total_jumps} jumps.")
        break

    elif jump > first_target_jump:
        first_target_jump += 5
        unsuccessful_jump_counter = 0

    else:
        unsuccessful_jump_counter += 1

    if unsuccessful_jump_counter == 3:
        print(f"Tihomir failed at {first_target_jump}cm after {total_jumps} jumps.")
        break
