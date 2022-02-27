days = 1
starting_point = 5_364
end_point = 8_848
while True:
    sleep = input()
    if sleep == "END":
        print("Failed!")
        print(starting_point)
        break
    meter_claimed = int(input())

    if sleep == "Yes":
        days += 1
        starting_point += meter_claimed
    else:
        starting_point += meter_claimed
    if days > 5:
        starting_point += -meter_claimed
    if starting_point >= end_point:
        print(f"Goal reached for {days} days!")
        break
    if days > 5:
        print("Failed!")
        print(starting_point)
        break

