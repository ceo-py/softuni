from collections import deque

amount_of_money = [int(x) for x in input().split()]
price_of_foods = deque(int(x) for x in input().split())
foods = 0

while amount_of_money and price_of_foods:
    money = amount_of_money.pop()
    price = price_of_foods.popleft()

    if money < price:
        continue

    if money > price:
        change = money - price
        if amount_of_money:
            amount_of_money[-1] += change
    foods += 1

if not foods:
    print("Henry remained hungry. He will try next weekend again.")
elif foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
else:
    print(f"Henry ate: {foods} food{'' if foods == 1 else 's'}.")

'''
input

9 5 8 18
18 12 10 5
'''

'''
output

Henry ate: 2 foods.

'''
