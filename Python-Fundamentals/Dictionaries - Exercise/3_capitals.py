country_name = input().split(", ")
capital_name = input().split(", ")

country_information = {country_name[i]: capital_name[i] for i in range(len(country_name))}

for country, capital in country_information.items():
    print(f"{country} -> {capital}")



# country_name = input().split(", ")
# capital_name = input().split(", ")
#
# country_information = {key: value for key, value in zip(country_name, capital_name)}
#
# for country, capital in country_information.items():
#     print(f"{country} -> {capital}")