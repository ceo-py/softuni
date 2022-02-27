movie_name = input()
number_days = int(input())
number_tickets = int(input())
price_ticket = float(input())
cinema_percent = int(input())

tickets_for_one_day = number_tickets * price_ticket
total_revenue = number_days * tickets_for_one_day
cinema_profit = total_revenue * cinema_percent / 100
total = total_revenue - cinema_profit

print(f"The profit from the movie {movie_name} is {total:.2f} lv.")
