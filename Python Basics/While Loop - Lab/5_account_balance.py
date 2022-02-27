total = 0
while True:
    money_deposit = input()
    if money_deposit[0] == "-":
        print("Invalid operation!")
        break
    elif money_deposit == "NoMoreMoney":
        break
    else:
        total += float(money_deposit)
        print("Increase:","{:.2f}".format(float(money_deposit)))
print(f"Total: {total:.2f}")
