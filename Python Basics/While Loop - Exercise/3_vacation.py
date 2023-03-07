needed_money = float(input())
available_money = float(input())
consecutive_spend_days = 0
days = 0

while available_money < needed_money and consecutive_spend_days < 5:
    action = input()
    amount = float(input())

    if action == 'save':
        available_money += amount
        consecutive_spend_days = 0
    elif action == 'spend':
        available_money -= amount
        consecutive_spend_days += 1

        if available_money < 0:
            available_money = 0

    days += 1

if consecutive_spend_days == 5:
    print("You can't save the money.")
    print(days)
else:
    print(f"You saved the money for {days} days.")






#
#
# holiday_price = float(input())
# available_money = float(input())
#
# days_count = 0
# total_money = available_money
# last_type_of_action = list()
# count = 0
# while True:
#     money_type = input()
#     money = float(input())
#     last_type_of_action.append(money_type)
#     days_count += 1
#     if money_type == "save":
#         total_money += + money
#     elif money_type == "spend":
#         total_money += - money
#         if total_money < 0:
#             total_money = 0
#     count = last_type_of_action.count("spend")
#     if count > 5 and last_type_of_action[-1] == "spend" and last_type_of_action[-2] == "spend" and \
#             last_type_of_action[-3] == "spend" and last_type_of_action[-4] == "spend" \
#             and money_type == "spend":
#         days_count += 1
#         print(f"You can't save the money.\n{days_count}")
#         break
#     if total_money >= holiday_price:
#         print(f"You saved the money for {days_count} days.")
#         break

#
# import sys
# money_needed = float(input())
# money_available = float(input())
#
# balance = money_available
# days_money_spent = 0
# total_days = 0
# cannot_spend = False
# while balance < money_needed:
# 	action = input()
# 	money = float(input())
# 	total_days += 1
#
# 	if action == "save":
# 		balance += money
# 		days_money_spent = 0
#
# 	elif action == "spend":
# 		days_money_spent += 1
# 		cannot_spend = days_money_spent == 5
# 		if cannot_spend:
# 			print(f"You can't save the money.")
# 			print(f"{total_days}")
# 			sys.exit()
#
# 		if money > balance:
# 			balance = 0
# 		else:
# 			balance -= money
#
# if balance >= money_needed:
# 	print(f"You saved the money for {total_days} days.")
#