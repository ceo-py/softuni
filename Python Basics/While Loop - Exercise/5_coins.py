change = float(input())
coins = 0
change = change * 100

currCoins = int(change / 200)
change -= currCoins * 200
coins += currCoins

currCoins = int(change / 100)
change -= currCoins * 100
coins += currCoins

currCoins = int(change / 50)
change -= currCoins * 50
coins += currCoins

currCoins = int(change / 20)
change -= currCoins * 20
coins += currCoins

currCoins = int(change / 10)
change -= currCoins * 10
coins += currCoins

currCoins = int(change / 5)
change -= currCoins * 5
coins += currCoins

currCoins = int(change / 2)
change -= currCoins * 2
coins += currCoins

currCoins = int(change)
coins += currCoins

print(coins)