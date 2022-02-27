mackerel_price_per_kg = float(input())
sprats_price_per_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())


mussels_kg_price = 7.50
total_mussels = mussels_kg * mussels_kg_price

bonito_kg_price = (((mackerel_price_per_kg * 0.60) + mackerel_price_per_kg) * bonito_kg)
horse_mackerel_price = (((sprats_price_per_kg * 0.80) + sprats_price_per_kg) * horse_mackerel_kg)

total_bill = total_mussels + bonito_kg_price + horse_mackerel_price

print(f"{total_bill:.2f}")
