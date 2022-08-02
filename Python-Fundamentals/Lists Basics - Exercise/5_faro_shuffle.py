cards = input().split()
shuffle = int(input())
middle_of_deck = len(cards) // 2

for number_of_shuffle in range(shuffle):
    cards = [c for pair in zip(cards[:middle_of_deck], cards[middle_of_deck:]) for c in pair]

print(cards)






#
# cards = input().split()
# shuffle = int(input())
# middle_of_deck = len(cards) // 2
#
# for number_of_shuffle in range(shuffle):
#     result_after_shuffle = []
#     for mid_card, front_card in enumerate(range(middle_of_deck), middle_of_deck):
#         result_after_shuffle.append(cards[front_card])
#         result_after_shuffle.append(cards[mid_card])
#     cards = result_after_shuffle.copy()
#
# print(cards)






# cards = input().split()
# shuffle = int(input())
#
# lenght = len(cards)
# mid = int(lenght / 2)
#
# for i in range(shuffle):
#     list = []
#     for p in range(0, mid):
#         list.append(cards[p])
#         list.append(cards[mid])
#         mid += 1
#     cards = list
#     mid = int(lenght / 2)
#
# print(list)