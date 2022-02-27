movie_name = input()
movie_extra = input()
movie_tickets = int(input())

extras = 0
off = 0
total = 0

if movie_name == "John Wick":

    if movie_extra == "Drink":
        extras += 12

    elif movie_extra == "Popcorn":
        extras += 15

    elif movie_extra == "Menu":
        extras += 19

elif movie_name == "Star Wars":

    if movie_extra == "Drink":
        extras += 18

    elif movie_extra == "Popcorn":
        extras += 25

    elif movie_extra == "Menu":
        extras += 30

elif movie_name == "Jumanji":

    if movie_extra == "Drink":
        extras += 9

    elif movie_extra == "Popcorn":
        extras += 11

    elif movie_extra == "Menu":
        extras += 14

total = extras * movie_tickets
if movie_tickets >= 4 and movie_name == "Star Wars":
    total = total - (total * 0.30)

elif movie_tickets == 2 and movie_name == "Jumanji":
    total = total - (total * 0.15)

print(f"Your bill is {total:.2f} leva.")
