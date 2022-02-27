cards = input().split()
shuffle = int(input())

lenght = len(cards)
mid = int(lenght / 2)

for i in range(shuffle):
    list = []
    for p in range(0, mid):
        list.append(cards[p])
        list.append(cards[mid])
        mid += 1
    cards = list
    mid = int(lenght / 2)

print(list)