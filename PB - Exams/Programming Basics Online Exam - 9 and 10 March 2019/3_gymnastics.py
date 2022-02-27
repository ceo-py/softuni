country = input()
type_device = input()

total_score = 0

if country == "Bulgaria" and type_device == "ribbon":
    total_score = 9.600 + 9.400
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Bulgaria" and type_device == "hoop":
    total_score = 9.550 + 9.750
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Bulgaria" and type_device == "rope":
    total_score = 9.500 + 9.400
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Russia" and type_device == "ribbon":
    total_score = 9.100 + 9.400
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Russia" and type_device == "hoop":
    total_score = 9.300 + 9.800
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Russia" and type_device == "rope":
    total_score = 9.600 + 9.000
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Italy" and type_device == "ribbon":
    total_score = 9.200 + 9.500
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Italy" and type_device == "hoop":
    total_score = 9.450 + 9.350
    points_left = 20 - total_score
    score = (points_left / 20) * 100

elif country == "Italy" and type_device == "rope":
    total_score = 9.700 + 9.150
    points_left = 20 - total_score
    score = (points_left / 20) * 100

print(f"The team of {country} get {total_score:.3f} on {type_device}.\n{score:.2f}%")
