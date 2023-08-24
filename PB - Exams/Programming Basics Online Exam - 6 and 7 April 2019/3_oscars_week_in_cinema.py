movie_name = input()
cinema_hall_type = input()
tickets_number = int(input())

price = 0

if movie_name == 'A Star Is Born':

    if cinema_hall_type == 'normal':
        price = 7.50

    elif cinema_hall_type == 'luxury':
        price = 10.50

    elif cinema_hall_type == 'ultra luxury':
        price = 13.50

elif movie_name == 'Bohemian Rhapsody':

    if cinema_hall_type == 'normal':
        price = 7.35

    elif cinema_hall_type == 'luxury':
        price = 9.45

    elif cinema_hall_type == 'ultra luxury':
        price = 12.75

elif movie_name == 'Green Book':

    if cinema_hall_type == 'normal':
        price = 8.15

    elif cinema_hall_type == 'luxury':
        price = 10.25

    elif cinema_hall_type == 'ultra luxury':
        price = 13.25

elif movie_name == 'The Favourite':

    if cinema_hall_type == 'normal':
        price = 8.75

    elif cinema_hall_type == 'luxury':
        price = 11.55

    elif cinema_hall_type == 'ultra luxury':
        price = 13.95

total_sum = price * tickets_number

print(f'{movie_name} -> {total_sum:.2f} lv.')






# movie_name = input()
# hall_type = input()
# number_tickes = int(input())
#
# movie_info = {
#     "A Star Is Born": {
#         "normal": 7.50,
#         "luxury": 10.50,
#         "ultra luxury": 13.50},
#     "Bohemian Rhapsody": {
#         "normal": 7.35,
#         "luxury": 9.45,
#         "ultra luxury": 12.75},
#     "Green Book": {
#         "normal": 8.15,
#         "luxury": 10.25,
#         "ultra luxury": 13.25},
#     "The Favourite": {
#         "normal": 8.75,
#         "luxury": 11.55,
#         "ultra luxury": 13.95},
#
# }
#
# total_price = movie_info[movie_name][hall_type] * number_tickes
#
# print(f"{movie_name} -> {total_price:.2f} lv.")