valcher = int(input())

item = input()
movie_tickets = 0
other_stuff = 0

while item != 'End':

    if len(item) > 8:
        valcher -= ord(item[1]) + ord(item[0])

        if valcher < 0:
            break

        movie_tickets += 1

    else:
        valcher -= ord(item[0])

        if valcher < 0:
            break

        other_stuff += 1

    item = input()

print(movie_tickets)
print(other_stuff)





# vouchers = int(input())
#
# total_money_left = vouchers
# movie_tickets_count = 0
# items_count = 0
# items = ""
#
# while True:
#     movie_ticket_price = 0
#     items_price = 0
#
#     items = input()
#     if items == "End" or total_money_left < 0:
#         print(f"{movie_tickets_count}\n{items_count}")
#         break
#
#     items_length = len(items)
#
#     if items_length > 8:
#         movie_ticket_price = ord(items[0]) + ord(items[1])
#         total_money_left += - movie_ticket_price
#
#         if total_money_left >= 0:
#             movie_tickets_count += 1
#
#         else:
#             if items == "End" or total_money_left < 0:
#                 print(f"{movie_tickets_count}\n{items_count}")
#                 break
#
#     elif items_length <= 8:
#         items_price = ord(items[0])
#         total_money_left += - items_price
#
#         if total_money_left >= 0:
#             items_count += 1
#
#         else:
#             if items == "End" or total_money_left < 0:
#                 print(f"{movie_tickets_count}\n{items_count}")
#                 break
