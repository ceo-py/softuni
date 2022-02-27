bitcoin = int(input())
chn = float(input())
fee = float(input())

bitcoin_price = 1168
chn_price = chn * 0.15
usd_price = 1.76
euro_price = 1.95
fee_number = fee / 100

bitcoin_total = bitcoin_price * bitcoin
chn_price = chn_price * usd_price
total_eur = (bitcoin_total + chn_price) / euro_price
fee_total_eur = total_eur * fee_number
total_result = total_eur - fee_total_eur

print("{:.2f}".format(total_result))
