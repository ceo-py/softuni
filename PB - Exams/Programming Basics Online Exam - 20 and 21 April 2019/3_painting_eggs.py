eggs_size = input()
eggs_color = input()
number_lots = int(input())

price = 0
expenses = 0.65

if eggs_size == 'Large':

    if eggs_color == 'Red':
        price = 16

    elif eggs_color == 'Green':
        price = 12

    elif eggs_color == 'Yellow':
        price = 9

elif eggs_size == 'Medium':

    if eggs_color == 'Red':
        price = 13

    elif eggs_color == 'Green':
        price = 9

    elif eggs_color == 'Yellow':
        price = 7

elif eggs_size == 'Small':

    if eggs_color == 'Red':
        price = 9

    elif eggs_color == 'Green':
        price = 8

    elif eggs_color == 'Yellow':
        price = 5

total = price * number_lots * expenses
print(f'{total:.2f} leva.')





# eggs_size = input()
# eggs_color = input()
# eggs_number = int(input())
#
# eggs_info = {
#     "Large": {
#         "Red": 16,
#         "Green": 12,
#         "Yellow": 9},
#     "Medium": {
#         "Red": 13,
#         "Green": 9,
#         "Yellow": 7},
#     "Small": {
#         "Red": 9,
#         "Green": 8,
#         "Yellow": 5},
# }
# total = eggs_info[eggs_size][eggs_color] * eggs_number
# total_profit = total - (total * 0.35)
# print(f"{total_profit:.2f} leva.")
