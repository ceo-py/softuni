def forecast(*аrgs):
    output, result = [], {"Sunny": [], "Cloudy": [], "Rainy": []}
    [result[key].append(town) for town, key in аrgs]
    [output.append(f"{names} - {key_}") for key_, town_ in result.items() for names in sorted(town_)]
    return "\n".join(output)




# def forecast(*аrgs):
#     output, result = [], {"Sunny" : [], "Cloudy": [], "Rainy": []}
#     [result[key].append(town) for town, key in аrgs]
#     for key_, town_ in result.items():
#         for names in sorted(town_):
#             output.append(f"{names} - {key_}")
#
#     return "\n".join(output)




print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))