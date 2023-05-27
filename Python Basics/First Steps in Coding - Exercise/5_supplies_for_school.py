pens_packs = int(input())
marker_packs = int(input())
detergent_liters = int(input())
discount = int(input()) / 100

pens_price = 5.80
marker_price = 7.20
detergent_price = 1.20

price_before_discount = (pens_packs * pens_price) + (marker_packs * marker_price) + (detergent_liters * detergent_price)
total_price = price_before_discount - price_before_discount * discount
print(total_price)



#
# a = int(input()) * 5.80
# b = int(input()) * 7.20
# c = int(input()) * 1.20
# d = int(input()) / 100
# print( a + b + c-(( a + b + c) * d ))
