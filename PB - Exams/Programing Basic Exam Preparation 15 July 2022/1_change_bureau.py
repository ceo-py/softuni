number_bitcoin = int(input())
number_china_yan = float(input())
commission = float(input())

one_bitcoin_price = 1168
one_china_yan_price = 0.15
usd_fixing = 1.76
eur_fixing = 1.95
fee = commission / 100

total_bitcoin = number_bitcoin * 1168
total_china_yan = (number_china_yan * one_china_yan_price) * usd_fixing
result = (total_bitcoin + total_china_yan) / eur_fixing
fee = result * fee
result -= fee

print(f"{result:.2f}")

