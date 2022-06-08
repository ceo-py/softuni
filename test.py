tickets_sting = input().replace(" ", "").split(",")

symbols = ['@', '#', '$', '^']
for ticket_characters in tickets_sting:
    price_find = False
    jackpot_find = False
    if len(ticket_characters) == 20:
        how_long = int(len(ticket_characters) / 2)
        left_side = ticket_characters[:how_long]
        right_side = ticket_characters[how_long:]
        if left_side == right_side and left_side[0] in symbols:
            print(f'ticket "{ticket_characters}" - 10{left_side[0]} Jackpot!')
            jackpot_find = True
        else:
            for index, symbol in enumerate(symbols):
                for symbols_number in range(9, 5, - 1):
                    if (symbol * symbols_number) in left_side and (symbol * symbols_number) in right_side:
                        symbol_type = symbols[index]
                        price_find = True
                        break
                if price_find:
                    print(f'ticket "{ticket_characters}" - {left_side.count(symbol_type)}{symbol_type}')
                    break
        if not jackpot_find and not price_find:
            print(f'ticket "{ticket_characters}" - no match')
    else:
        print("invalid ticket")

# tickets = input().replace(" ", "")
# tickets = tickets.split(',')
# count = 0
# symb = ''
# symbols = ['@', '#', '$', '^']
#
# for ticket in tickets:
#     fins_ticket = False
#     if len(ticket) != 20:
#         print('invalid ticket')
#         continue
#     left = ticket[:int(len(ticket) / 2)]
#     right = ticket[int(len(ticket) / 2):]
#     for index, sym in enumerate(symbols):
#         if 6 * sym in left and 6 * sym in right:
#             count = 0
#             for i in range(7, 11):
#                 if (i * sym) in left and (i * sym) in right:
#                     count += 1
#             symb = symbols[index]
#             fins_ticket = True
#     if not fins_ticket:
#         print(f'ticket "{ticket}" - no match')
#     elif count != 4:
#         print(f'ticket "{ticket}" - {6 + count}{symb}')
#     else:
#         print(f'ticket "{ticket}" - {6 + count}{symb} Jackpot!')


# tickets = input().replace(" ", "")
# tickets = tickets.split(',')
# count = 0
# symb = ''
# symbols = ['@', '#', '$', '^']
#
# def check_next(symbol, first, second):
#     back = 6
#     for i in range(7, 11):
#         if (i * symbol) in first and (i * symbol) in second:
#             back += 1
#     return back
#
#
# for ticket in tickets:
#     fins_ticket =False
#     if len(ticket) != 20:
#         print('invalid ticket')
#         continue
#     left = ticket[0:int(len(ticket) / 2)]
#     right = ticket[int(len(ticket) / 2):]
#     for index, sym in enumerate(symbols):
#         if (6 * sym) in left and (6 * sym) in right:
#             count = check_next(sym, left, right)
#             symb = symbols[index]
#             fins_ticket = True
#     if not fins_ticket:
#         print(f'ticket "{ticket}" - no match')
#     elif count != 10:
#         print(f'ticket "{ticket}" - {count}{symb}')
#     else:
#         print(f'ticket "{ticket}" - {count}{symb} Jackpot!')
