total = 0
money_deposit = input()

while money_deposit != 'NoMoreMoney':
    money_deposit = float(money_deposit)
    if money_deposit < 0:
        print("Invalid operation!")
        break

    total += money_deposit
    print(f"Increase: {money_deposit:.2f}")
    money_deposit = input()

print(f"Total: {total:.2f}")





# total = 0
# while True:
#     money_deposit = input()
#     if money_deposit[0] == "-":
#         print("Invalid operation!")
#         break
#     elif money_deposit == "NoMoreMoney":
#         break
#     else:
#         total += float(money_deposit)
#         print("Increase:","{:.2f}".format(float(money_deposit)))
# print(f"Total: {total:.2f}")
