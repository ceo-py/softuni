weather_celcius = float(input())

if weather_celcius <= 5.00 or weather_celcius > 35:
    print("unknown")
elif weather_celcius <= 11.9:
    print("Cold")
elif weather_celcius <= 14.90:
    print("Cool")
elif weather_celcius <= 20.00:
    print("Mild")
elif weather_celcius <= 25.90:
    print("Warm")
elif weather_celcius <= 35.00:
    print("Hot")


    

    
# import numpy as np
#
# temperature = float(input())
# correct_time = False
# degrees = {
#     "Hot": [f"{n:.1f}" for n in np.arange(26.0, 35.1, 0.1)],
#     "Warm": [f"{n:.1f}" for n in np.arange(21.0, 26, 0.1)],
#     "Mild": [f"{n:.1f}" for n in np.arange(15.0, 20.1, 0.1)],
#     "Cool": [f"{n:.1f}" for n in np.arange(12.0, 15, 0.1)],
#     "Cold": [f"{n:.1f}" for n in np.arange(5.0, 12, 0.1)],
# }
#
# for weather, temp in degrees.items():
#     if f"{temperature:.1f}" in temp:
#         print(weather)
#         correct_time = True
#
# if not correct_time:
#     print("unknown")




# temperature = float(input())
# correct_time = False
# degrees = {
#     "unknown": [temperature <= 5.00 or temperature > 35.00],
#     "Hot": [26.00 <= temperature <= 35.00],
#     "Warm": [20.1 <= temperature <= 25.90],
#     "Mild": [15.00 <= temperature <= 20.00],
#     "Cool": [12.00 <= temperature <= 14.90],
#     "Cold": [5.00 < temperature <= 11.9],
# }
# 
# for weather, temp in degrees.items():
#     if any(temp):
#         print(weather)
#         break    
    
