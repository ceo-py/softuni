hours = int(input())
minutes = int(input())

minutes_added = 15
total_minutes = minutes_added + minutes

if total_minutes > 59:
    over_sixty_minutes = total_minutes - 60
    total_time = hours + 1
    if total_time >= 24:
        total_time = 0
        if over_sixty_minutes < 10:
            print(f"{total_time}:0{over_sixty_minutes}")
        else:
            print(f"{total_time}:{over_sixty_minutes}")
    else:
        if over_sixty_minutes < 10:
            print(f"{total_time}:0{over_sixty_minutes}")
        else:
            print(f"{total_time}:{over_sixty_minutes}")
    total_minutes = minutes_added + minutes
elif total_minutes < 10:
    print(f"{hours}:0{total_minutes}")
else:
    print(f"{hours}:{total_minutes}")
