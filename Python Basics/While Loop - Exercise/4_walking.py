total_steps = 0
goal = 10000
while True:
    steps_walk = input()
    if steps_walk == "Going home":
        steps_walk_in_a_day = int(input())
        total_steps += steps_walk_in_a_day
        if total_steps >= goal:
            total_steps += - goal
            print(f"Goal reached! Good job!\n{total_steps} steps over the goal!")
            break
        else:
            total_steps = goal - total_steps
            print(f"{total_steps} more steps to reach goal.")
            break
    total_steps += int(steps_walk)

    if total_steps >= goal:
        total_steps += - goal
        print(f"Goal reached! Good job!\n{total_steps} steps over the goal!")
        break
