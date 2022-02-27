weather_celcius = float(input())

if weather_celcius <= 5.00:
    print("unknown")
elif 5.00 <= weather_celcius <= 11.9:
    print("Cold")
elif weather_celcius <= 14.90:
    print("Cool")
elif weather_celcius <= 20.00:
    print("Mild")
elif weather_celcius <= 25.90:
    print("Warm")
elif weather_celcius <= 35.00:
    print("Hot")
else:
    print("unknown")
