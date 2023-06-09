air_line = input()
adults_ticket_number = int(input())
kids_ticket_number = int(input())
adults_ticket_price = float(input())
tax = float(input())

adults_sum = adults_ticket_number * (adults_ticket_price + tax)
kids_sum = kids_ticket_number * (adults_ticket_price * 0.30 + tax)
total_sum = (kids_sum + adults_sum) * 0.20

print(f'The profit of your agency from {air_line} tickets is {total_sum:.2f} lv.')




air_comapy_name = input()
adult_tickets = int(input())
kids_tickets = int(input())
net_price_adult_tickets = float(input())
fee_services = float(input())

kids_tickets_off = 0.70
proftif_margin = 0.20

net_price_kids_tickets = net_price_adult_tickets - net_price_adult_tickets * kids_tickets_off
adult_tickets_fee = net_price_adult_tickets + fee_services
kids_tickets_fee = net_price_kids_tickets + fee_services
total_price_tickets = adult_tickets * adult_tickets_fee + kids_tickets_fee * kids_tickets

profit = "{:.2f}".format(total_price_tickets * proftif_margin)

print(f"The profit of your agency from {air_comapy_name} tickets is {profit} lv.")


