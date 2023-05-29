budget = int(input())
price = input()

while price != "End":
    budget -= int(price)
    if budget < 0:
        print("You went in overdraft!")
        break
    price = input()
else:
    print("You bought everything needed.")



# budget = int(input())
# money = input()
# while money != "End":
#
#     product = int(money)
#     budget = budget - product
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     money = input()
#
# else:
#     print("You bought everything needed.")
