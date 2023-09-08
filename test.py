# budget = float(input())
#
# product = input()
# product_counter = 0
# starting_budget = budget
#
# while product != 'Stop':
#     price = float(input())
#     product_counter += 1
#
#     if product_counter % 3 == 0:
#         price *= 0.50
#
#     if budget - price >= 0:
#         budget -= price
#     else:
#         print("You don't have enough money!")
#         print(f"You need {abs(budget - price):.2f} leva!")
#         break
#
#     product = input()
#
# else:
#     print(f'You bought {product_counter} products for {abs(budget - starting_budget):.2f} leva.')


budget = float(input())
command = input()
leaving_budget = budget
counter = 0
while command != 'Stop':
    price = float(input())
    counter += 1

    if counter % 3 == 0:
        price *= 0.50

    budget -= price
    if budget < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break

    command = input()

if command == 'Stop':
    print(f"You bought {counter} products for {abs(budget - leaving_budget):.2f} leva.")