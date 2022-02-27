season = input()
km_per_mouth = int(input())

taxes = 0.10

if season == "Spring" or season == "Autumn":
    if km_per_mouth <= 5000:
        total = km_per_mouth * 0.75
    if 5000 < km_per_mouth <= 10000:
        total = km_per_mouth * 0.95
if season == "Summer":
    if km_per_mouth <= 5000:
        total = km_per_mouth * 0.90
    if 5000 < km_per_mouth <= 10000:
        total = km_per_mouth * 1.10
if season == "Winter":
    if km_per_mouth <= 5000:
        total = km_per_mouth * 1.05
    if 5000 < km_per_mouth <= 10000:
        total = km_per_mouth * 1.25

if 10000 < km_per_mouth <= 20000:
    total = km_per_mouth * 1.45

total = (total - (total * taxes)) * 4
print(f"{total:.2f}")
