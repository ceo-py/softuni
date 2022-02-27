holiday_price = float(input())
available_money = float(input())

days_count = 0
total_money = available_money
last_type_of_action = list()
count = 0
while True:
    money_type = input()
    money = float(input())
    last_type_of_action.append(money_type)
    days_count += 1
    if money_type == "save":
        total_money += + money
    elif money_type == "spend":
        total_money += - money
        if total_money < 0:
            total_money = 0
    count = last_type_of_action.count("spend")
    if count > 5 and last_type_of_action[-1] == "spend" and last_type_of_action[-2] == "spend" and \
            last_type_of_action[-3] == "spend" and last_type_of_action[-4] == "spend" \
            and money_type == "spend":
        days_count += 1
        print(f"You can't save the money.\n{days_count}")
        break
    if total_money >= holiday_price:
        print(f"You saved the money for {days_count} days.")
        break
