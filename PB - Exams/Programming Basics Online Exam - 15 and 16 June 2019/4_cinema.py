capacity_hall = int(input())

ticket_price = 5
total_price_tickets = 0
total_tickets_sell = 0
tickets_left = capacity_hall

while True:

    people_in_cinema = input()
    total_tickets_sell += 1
    if people_in_cinema == "Movie time!":
        print(f"There are {tickets_left} seats left in the cinema.\nCinema income - {total_price_tickets} lv.")
        break

    people_in_cinema = int(people_in_cinema)
    tickets_left -= people_in_cinema
    if tickets_left < 0:
        print(f"The cinema is full.\nCinema income - {total_price_tickets} lv.")
        break

    if people_in_cinema % 3 == 0:
        total_price_tickets += (people_in_cinema * ticket_price) - 5

    else:
        total_price_tickets += (people_in_cinema * ticket_price)


