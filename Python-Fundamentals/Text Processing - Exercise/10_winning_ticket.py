import re


tickets_sting = input().split(", ")
symbols = ['@', '#', '$', '^']


for ticket_characters in tickets_sting:
    ticket_characters = ticket_characters.replace(" ", "")
    if len(ticket_characters) == 20:
        how_long = int(len(ticket_characters) / 2)
        left_side, right_side = ticket_characters[:how_long], ticket_characters[how_long:]
        for symbol in symbols:
            opz = f"\{symbol}+"
            try:
                l_occurs = max([len(i) for i in re.findall(opz, left_side)])
                r_occurs = max([len(i) for i in re.findall(opz, right_side)])
            except ValueError:
                continue
            if l_occurs == r_occurs == 10:
                print(f'ticket "{ticket_characters}" - 10{symbol} Jackpot!')
                break
            winners_price = min(l_occurs, r_occurs)
            if winners_price >= 6:
                print(f'ticket "{ticket_characters}" - {winners_price}{symbol}')
                break
        else:
            print(f'ticket "{ticket_characters}" - no match')
    else:
        print("invalid ticket")









# tickets_sting = input().split(", ")
#
# symbols = ['@', '#', '$', '^']
#
#
# def check_next(symbol, first, second):
#     back = 6
#     for i in range(7, 11):
#         if (i * symbol) in first and (i * symbol) in second:
#             back += 1
#     return back
#
#
# for ticket_characters in tickets_sting:
#     price_find = False
#     jackpot_find = False
#     ticket_characters = ticket_characters.replace(" ", "")
#     if len(ticket_characters) == 20:
#         how_long = int(len(ticket_characters) / 2)
#         left_side = ticket_characters[:how_long]
#         right_side = ticket_characters[how_long:]
#         for index, symbol in enumerate(symbols):
#             if 10 * symbol in left_side and 10 * symbol in right_side:
#                 print(f'ticket "{ticket_characters}" - 10{symbols[index]} Jackpot!')
#                 jackpot_find = True
#                 break
#             elif 6 * symbol in left_side and 6 * symbol in right_side:
#                 symbol_type = symbols[index]
#                 total = check_next(symbol_type, left_side, right_side)
#                 price_find = True
#                 break
#         if price_find:
#             print(f'ticket "{ticket_characters}" - {total}{symbol_type}')
#         elif not jackpot_find and not price_find:
#             print(f'ticket "{ticket_characters}" - no match')
#     else:
#         print("invalid ticket")




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