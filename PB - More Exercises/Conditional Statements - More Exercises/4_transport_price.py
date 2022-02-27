numbers_of_kilometers = int(input())
day_type = input()

taxi_inicial = 0.70
taxi_day_tariff = 0.79
taxi_night_tariff = 0.90
bus_tax = 0.09
train = 0.06
total = 0

if numbers_of_kilometers < 20:
    if day_type == "day":
        total = taxi_inicial + numbers_of_kilometers * taxi_day_tariff
    else:
        total = taxi_inicial + numbers_of_kilometers * taxi_night_tariff
elif numbers_of_kilometers < 100:
    total = numbers_of_kilometers * bus_tax
elif numbers_of_kilometers >= 100:
    total = numbers_of_kilometers * train

print(f"{total:.2f}")
