expected_sum_to_be_colected = int(input())
command = input()

payment_type, cash_payment, card_payment,cash_count, card_count = 0, 0, 0, 0, 0


while command != "End":
    payment_type += 1
    product_price = int(command)

    # логика за неуспешни плащания
    if product_price > 100 and payment_type % 2 != 0 or \
            product_price <= 10 and payment_type % 2 == 0:
        print("Error in transaction!")

    # логика за успешни плащания
    elif product_price <= 100 and payment_type % 2 != 0:
        cash_payment += product_price
        cash_count += 1
        print("Product sold!")
    elif product_price > 10 and payment_type % 2 == 0:
        card_payment += product_price
        card_count += 1
        print("Product sold!")

    # логика за ако плащанията са стигнали
    total_payment = card_payment + cash_payment
    if total_payment >= expected_sum_to_be_colected:
        print(f"Average CS: {cash_payment / cash_count:.2f}")
        print(f"Average CC: {card_payment / card_count:.2f}")
        break

    command = input()


else:
    print("Failed to collect required money for charity.")






#
# card_counter = 0
# counter = 0
#
# input_line = input()
# while input_line != "End":
#     money = int(input_line)
#     if money == int(input_line):
#         counter += 1
#
#     if counter % 2 == 0:
#         if money < 10:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             collected += money
#             card += money
#             card_counter += 1
#     else:
#         if money > 100:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             collected += money
#             cash += money
#             cash_counter += 1
#
#     if  collected >= sum_needed:
#         average_cash = cash / cash_counter
#         average_card = card / card_counter
#         print(f"Average CS: {average_cash:.2f}")
#         print(f"Average CC: {average_card:.2f}")
#         break
#
#     input_line = input()
#
# else:
#     print("Failed to collect required money for charity.")
#



# expected_sum_to_be_colected = int(input())
#
#
# command = input()
# payment_type = 0 # 1 е плащане с кеш, 2 е плащане с карта
# cash_payment = 0
# card_payment = 0
#
# cash_count = 0
# card_count = 0
#
#
# while command != "End":
#     payment_type += 1
#     product_price = int(command)
#
#     # логика за неуспешни плащания
#     if product_price > 100 and payment_type == 1:
#         print("Error in transaction!")
#     elif product_price <= 10 and payment_type == 2:
#         print("Error in transaction!")
#     # логика за успешни плащания
#
#     if product_price <= 100 and payment_type == 1:
#         cash_payment += product_price
#         cash_count += 1
#         print("Product sold!")
#     elif product_price > 10 and payment_type == 2:
#         card_payment += product_price
#         card_count += 1
#         print("Product sold!")
#
#     # логика за ако плащанията са стигнали
#     total_payment = card_payment + cash_payment
#     if total_payment >= expected_sum_to_be_colected:
#         print(f"Average CS: {cash_payment/cash_count:.2f}")
#         print(f"Average CC: {card_payment / card_count:.2f}")
#         break
#
#     # резетване на метода на плащане
#     if payment_type == 2:
#         payment_type = 0
#
#     command = input()
#
#
# else:
#     print("Failed to collect required money for charity.")






#
#
# expected_sum = int(input())
#
# cash_payment = 0
# card_payment = 0
# total_items = 0
# sum_left = expected_sum
# card_count = 0
# cash_count = 0
#
# while True:
#     total_sum = cash_payment + card_payment
#     if total_sum >= expected_sum:
#         cash_payment = cash_payment / cash_count
#         card_payment = card_payment / card_count
#         print(f"Average CS: {cash_payment:.2f}\nAverage CC: {card_payment:.2f}")
#         break
#     sum_to_be_colected = input()
#     if sum_to_be_colected == "End":
#         print("Failed to collect required money for charity.")
#         break
#     sum_to_be_colected = int(sum_to_be_colected)
#     total_items += sum_to_be_colected
#     if sum_to_be_colected <= 100:
#         sum_left += + sum_to_be_colected
#         cash_payment += sum_to_be_colected
#         cash_count += 1
#         print("Product sold!")
#     else:
#         print(f"Error in transaction!")
#     sum_to_be_colected = input()
#     if sum_to_be_colected == "End":
#         print("Failed to collect required money for charity.")
#         break
#     sum_to_be_colected = int(sum_to_be_colected)
#     if sum_to_be_colected <= 10:
#         print(f"Error in transaction!")
#     else:
#         sum_left += + sum_to_be_colected
#         card_payment += +sum_to_be_colected
#         card_count += 1
#         print("Product sold!")
